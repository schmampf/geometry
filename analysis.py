import numpy as np
from numpy.typing import NDArray

from shapely import MultiPolygon
from tqdm import tqdm

from shapely.affinity import rotate
from shapely.geometry import Polygon

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.colors import ListedColormap

from geometry import to_polygons
from geometry import circle


def aperture_analysis(
    shape1: MultiPolygon,
    shape2: MultiPolygon,
    r_lim: tuple[float, float] = (0.0, 10.0),
    theta_lim: tuple[float, float] = (0.0, 30.0),
) -> tuple[
    NDArray[np.float64],
    NDArray[np.float64],
    NDArray[np.float64],
    NDArray[np.float64],
    NDArray[np.float64],
]:

    radii = np.linspace(r_lim[0], r_lim[1], 101, dtype=np.float64)  # cm
    degrees = np.linspace(theta_lim[0], theta_lim[1], 61, dtype=np.float64)  # deg

    dr = (np.max(radii) - np.min(radii)) / (len(radii) - 1)

    rings: list[Polygon] = []
    ring_areas: NDArray[np.float64] = np.zeros_like(radii, dtype="float64")

    for j, r in enumerate(radii):
        circle1 = circle(r=max(r - dr / 2, r_lim[0]), n_points=360)
        circle2 = circle(r=min(r + dr / 2, r_lim[1]), n_points=360)
        ring = to_polygons(circle2.difference(circle1))[0]
        ring_areas[j] = ring.area
        rings.append(ring)

    A_r_theta = np.zeros((len(radii), len(degrees)), dtype=np.float64)
    for i, angle_deg in enumerate(tqdm(degrees)):
        tmp_shape2 = rotate(shape2, angle_deg)
        tmp_shape0 = shape1.buffer(0).intersection(tmp_shape2.buffer(0))

        for j, r in enumerate(radii):
            tmp_slice = tmp_shape0.intersection(rings[j])
            A_r_theta[j, i] = tmp_slice.area  # cm2

    f_tot = np.sum(A_r_theta, axis=0) / (r_lim[1] ** 2 * np.pi) * 1e2  # %
    r_com = np.sum(radii[:, np.newaxis] * A_r_theta, axis=0) / np.sum(
        A_r_theta, axis=0
    )  # cm

    return radii, degrees, A_r_theta, f_tot, r_com


def visualize_analysis(
    radii: NDArray[np.float64],
    degrees: NDArray[np.float64],
    A_r_theta: NDArray[np.float64],
    f_tot: NDArray[np.float64],
    r_com: NDArray[np.float64],
    cmap: str | ListedColormap = "viridis",
    color_com: str = "red",
    color_area: str = "darkred",
) -> tuple[Figure, tuple[Axes, Axes, Axes, Axes]]:

    radians = np.deg2rad(degrees)  # rad

    dr = (np.max(radii) - np.min(radii)) / (len(radii) - 1)
    ddeg = (np.max(degrees) - np.min(degrees)) / (len(degrees) - 1)
    drad = (np.max(radians) - np.min(radians)) / (len(radians) - 1)

    ext_deg = (
        degrees[0] - ddeg / 2,
        degrees[-1] + ddeg / 2,
        radii[0] - dr / 2,
        radii[-1] + dr / 2,
    )
    ext_rad = (
        radians[0] - drad / 2,
        radians[-1] + drad / 2,
        ext_deg[2],
        ext_deg[3],
    )

    fig = plt.figure(0, figsize=(10, 4))
    gs = fig.add_gridspec(
        2, 2, width_ratios=[5, 4], hspace=0.3, wspace=0.1, height_ratios=[4, 0.2]
    )

    ax_kar = fig.add_subplot(gs[0, 0])
    ax_rad = fig.add_subplot(gs[0, 1], projection="polar")
    ax_clb = fig.add_subplot(gs[1, 0])
    ax_kar2 = ax_kar.twinx()

    im = ax_kar.imshow(
        A_r_theta,
        extent=ext_deg,
        origin="lower",
        aspect="auto",
        cmap=cmap,
    )
    im = ax_rad.imshow(
        A_r_theta,
        extent=ext_rad,
        origin="lower",
        aspect="auto",
        cmap=cmap,
    )
    clb = fig.colorbar(im, cax=ax_clb, orientation="horizontal")
    ax_kar.plot(degrees, r_com, lw=2, color=color_com, label="$r_{\\mathrm{COM}}$")
    ax_kar2.plot(degrees, f_tot, lw=2, color=color_area)

    ax_rad.plot(radians, r_com, lw=2, color=color_com)

    n0, n1 = ax_kar2.get_ylim()

    ax_rad.plot(radians, (f_tot - n0) / (n1 - n0) * ext_deg[3], lw=2, color=color_area)

    ax_kar.set_xlabel("$\\theta_\\mathrm{rot}$ (deg)")
    ax_kar.set_ylabel("$r$ (cm)")
    ax_kar2.set_ylabel("$f_\\mathrm{tot}$ (%)", color=color_area)
    clb.set_label("$A(r, \\theta)$ (cm$^2$)")
    ax_kar.legend()

    ax_kar.tick_params(direction="in", left=True, right=False, top=True, bottom=True)
    ax_rad.tick_params(direction="in", left=True, right=True, top=True, bottom=True)
    ax_kar2.tick_params(
        direction="in",
        left=False,
        right=True,
        top=True,
        bottom=True,
        color=color_area,
        labelcolor=color_area,
    )
    ax_kar.xaxis.set_ticks_position("top")
    ax_kar.xaxis.set_label_position("top")

    ax_rad.set_xlim((ext_rad[0], ext_rad[1]))
    ax_rad.set_theta_zero_location("N")
    ax_rad.set_theta_direction(-1)
    ax_rad.set_yticklabels([])
    ax_rad.grid(False)

    return fig, (ax_kar, ax_kar2, ax_rad, ax_clb)


"""
old visualization

# # show analysis results

# fig = plt.figure(0, figsize=(10, 8))
# gs = fig.add_gridspec(
#     2, 3, height_ratios=[4, 4], width_ratios=[5, 4, 0.2], hspace=0.3, wspace=0.1
# )

# ax1_kar = fig.add_subplot(gs[0, 0])
# ax1_rad = fig.add_subplot(gs[0, 1], projection="polar")
# ax1_clb = fig.add_subplot(gs[0, 2])

# ax2_kar = fig.add_subplot(gs[1, 0])
# ax2_rad = fig.add_subplot(gs[1, 1], projection="polar")
# ax2_clb = fig.add_subplot(gs[1, 2])

# cmap1 = "viridis"  # cmap(color="seeblau", inverse=True)
# cmap2 = "viridis"  # cmap(color="seegrün", inverse=True)

# color_com = "red"  # colors(2)
# color_area = "darkred"  # colors(3)

# im1 = ax1_kar.imshow(
#     A_r,
#     extent=ext_deg,
#     origin="lower",
#     aspect="auto",
#     cmap=cmap1,
# )
# im1 = ax1_rad.imshow(
#     A_r,
#     extent=ext_rad,
#     origin="lower",
#     aspect="auto",
#     cmap=cmap1,
# )
# clb1 = fig.colorbar(im1, cax=ax1_clb)

# im2 = ax2_kar.imshow(
#     N_r,
#     extent=ext_deg,
#     origin="lower",
#     aspect="auto",
#     cmap=cmap2,
# )
# im2 = ax2_rad.imshow(
#     N_r,
#     extent=ext_rad,
#     origin="lower",
#     aspect="auto",
#     cmap=cmap2,
# )
# clb2 = fig.colorbar(im2, cax=ax2_clb)

# for ax in [ax1_kar, ax1_rad, ax2_kar, ax2_rad]:
#     ax.tick_params(direction="in", left=True, right=True, top=True, bottom=True)

# for ax in [ax1_rad, ax2_rad]:
#     ax.plot(radians, r_com, lw=2, color=color_com)
#     ax.set_xlim((ext_rad[0], ext_rad[1]))
#     ax.set_theta_zero_location("N")
#     ax.set_theta_direction(-1)
#     ax.grid(False)
#     ax.set_yticklabels([])

# for ax in [ax1_kar, ax2_kar]:
#     ax.plot(degrees, r_com, lw=2, color=color_com)
#     ax.set_xlabel("$\\theta_\\mathrm{rot}$ (deg)")
#     ax.set_ylabel("$r$ (cm)")
#     ax.xaxis.set_ticks_position("top")
#     ax.xaxis.set_label_position("top")
#     ax2 = ax.twinx()
#     ax2.plot(degrees, A_rel, lw=2, color=color_area)
#     ax2.tick_params(
#         direction="in",
#         left=False,
#         right=True,
#         top=True,
#         bottom=True,
#         color=color_area,
#         labelcolor=color_area,
#     )
#     ax2.set_ylabel("$A_\\mathrm{rel}$ (%)", color=color_area)

# clb1.set_label("$A$ (cm$^2$)")
# clb2.set_label("$A(r, \\theta) / \\langle A\\rangle_r(\\theta)$ (arb.u.)")
"""
