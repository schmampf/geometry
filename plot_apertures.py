from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
from shapely.plotting import plot_polygon
from shapely.affinity import rotate
from geometry import annular_wedge_polygon

import numpy as np

from matplotlib.animation import FuncAnimation

from shapely.geometry import Polygon


def show_apertures(
    aperture1: list[Polygon],
    aperture2: list[Polygon],
    circle0: Polygon,
    r_lim: tuple[float, float] = (0.0, 10.0),
    theta_lim: tuple[float, float] = (0.0, 30.0),
) -> tuple[Figure, Axes]:
    wedge = annular_wedge_polygon(*r_lim, *theta_lim)
    fig, ax = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=(5, 5),
    )

    plot_polygon(
        circle0,
        ax=ax,
        add_points=False,
        color="black",
        fill=False,
        zorder=2,
    )
    plot_polygon(
        wedge,
        ax=ax,
        add_points=False,
        edgecolor="k",
        fill=False,
        alpha=1,
        label="rotation zone",
        zorder=2,
    )
    for j, poly in enumerate(aperture1):
        plot_polygon(
            poly,
            ax=ax,
            add_points=False,
            fill=True,
            color="C0",
            alpha=0.4,
            label="aperture 1" if j == 0 else None,
        )
    for j, poly in enumerate(aperture2):
        plot_polygon(
            poly,
            ax=ax,
            add_points=False,
            fill=True,
            color="C1",
            alpha=0.4,
            label="aperture 2" if j == 0 else None,
        )

    ax.axis("equal")
    ax.set_xlabel("$x$ (cm)")
    ax.set_ylabel("$y$ (cm)")
    ax.legend(loc="upper right", fontsize=8)

    return fig, ax


def animate_apertures(
    aperture1: list[Polygon],
    aperture2: list[Polygon],
    circle0: Polygon,
    r_lim: tuple[float, float] = (0.0, 10.0),
    theta_lim: tuple[float, float] = (0.0, 30.0),
) -> tuple[Figure, Axes, FuncAnimation]:
    wedge = annular_wedge_polygon(*r_lim, *theta_lim)
    fig, ax = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=(5, 5),
    )

    plot_polygon(
        circle0,
        ax=ax,
        add_points=False,
        color="black",
        fill=False,
        zorder=2,
    )

    plot_polygon(
        wedge,
        ax=ax,
        add_points=False,
        fill=True,
        facecolor="lightgrey",
        edgecolor="grey",
        alpha=0.5,
    )

    patch_wedge = plot_polygon(
        annular_wedge_polygon(
            r_inner=r_lim[0],
            r_outer=r_lim[1],
            start_angle_deg=theta_lim[0],
            end_angle_deg=theta_lim[0],
        ),
        ax=ax,
        add_points=False,
        edgecolor="k",
        fill=False,
        alpha=1,
        label="rotation zone",
        zorder=10,
    )

    for j, poly in enumerate(aperture1):
        plot_polygon(
            poly,
            ax=ax,
            add_points=False,
            color="C0",
            alpha=0.4,
            label="aperture 1" if j == 0 else None,
        )

    patches2: list[PathPatch] = []
    for j, poly in enumerate(aperture2):
        patches2.append(
            plot_polygon(
                poly,
                ax=ax,
                add_points=False,
                color="C1",
                alpha=0.4,
                label="aperture 2" if j == 0 else None,
            )
        )
    patches2.append(patch_wedge)

    ax.set_aspect("equal")
    ax.set_xlabel("$x$ (cm)")
    ax.set_ylabel("$y$ (cm)")
    ax.legend(loc="upper right", fontsize=8)

    # --- animation update function ---
    def update(frame_angle: int):
        for i, poly in enumerate(aperture2):
            patches2[i].remove()
            poly = rotate(poly, frame_angle, origin=(0, 0))
            patches2[i] = plot_polygon(
                poly, ax=ax, add_points=False, color="C1", alpha=0.4
            )

        patches2[-1].remove()
        patches2[-1] = plot_polygon(
            annular_wedge_polygon(
                r_inner=r_lim[0],
                r_outer=r_lim[1],
                start_angle_deg=theta_lim[0],
                end_angle_deg=frame_angle,
            ),
            ax=ax,
            edgecolor="k",
            add_points=False,
            fill=False,
            zorder=10,
        )
        return patches2

    # --- create and display animation ---
    angles = np.linspace(
        theta_lim[0], theta_lim[1], 90
    )  # 60 frames from 0 to 90 degrees
    anim = FuncAnimation(
        fig, update, frames=angles, blit=True, interval=15, repeat=True
    )

    return fig, ax, anim
