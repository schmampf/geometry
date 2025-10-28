# Geometry: Dynamic Aperture Design

This project explores the geometric optimization of a variable aperture system, inspired by observations of an ethanol stove's flame control mechanism. The goal is to create a safer and more efficient method of controlling combustion through precisely designed geometric patterns.

## Project Overview

Traditional ethanol stoves use a sliding plate mechanism to control the flame, which can be hazardous due to proximity to the heat source. This project proposes an innovative solution: two superimposed plates with specially designed apertures that can be rotated relative to each other. This rotation creates a dynamic opening pattern that transitions from a small central aperture to an expanding ring, allowing precise control over the combustion process.

## Physical Parameters

The system is described in both Cartesian $(x,y)$ and polar $(r,\theta)$ coordinates, where:

$R$: outer radius of aperture.

$A(r, \theta)$: Combined aperture area within an annular ring at radius $r$ (width $\mathrm{d}r$, circumference $2\pi r$) for rotation angle $\theta$ in cm $^2$.

$A_\mathrm{tot}(\theta) = \sum_{r=0}^{R} A(r, \theta)$: Total combined aperture area at rotation angle $\theta$ in cm $^2$.

$f(r, \theta) = \frac{A(r, \theta)}{\pi r\mathrm{d}r}$: Combined aperture area within an annular ring, normalized by ring geometry. This describes the local density of openings at radius $r$.

$f_\mathrm{tot}(\theta) = \frac{\sum_{r=0}^{R} A(r, \theta)}{\pi R^2}$: Relative total combined aperture area.

$r_\mathrm{com}(\theta) = \frac{\sum_{r=0}^{R} r \cdot A(r, \theta)}{\sum_{r=0}^{R} A(r, \theta)}$: Center of mass radius of the combined aperture area in cm.

Target parameter ranges for optimal combustion control:

- $\theta \in [0, 30]$ deg
- $f_\mathrm{tot}(\theta) \in [0, 20]$ %
- $r_\mathrm{com}(\theta) \in [0, R]$

The design aims for monotonic growth in both $r_\mathrm{com}$ and $f_\mathrm{tot}$ as $\theta$ increases, ensuring smooth and predictable combustion control.

## Current Development Status

At first an analysis and visualization tool has been developed.

While simple geometric solutions like spiral patterns are possible, this project explores more sophisticated approaches:

1. Implementation of 2D grids and monohedral tilings
2. Investigation of Moiré patterns inspired by twisted bilayer graphene
3. Exploration of 2D quasicrystals and Penrose tilings

The current focus is on understanding and implementing quasicrystal patterns, which offer unique geometric properties that could provide optimal aperture control. This investigation has led to deep theoretical study, including detailed analysis of Penrose tiling systems and their applications to this specific problem.

### Twisted Bilayer Graphene

Here we can see increasing $f_\mathrm{tot}$, however $r_\mathrm{com}$ isn't moving at all.

![twisted bilayer graphene animation](https://github.com/schmampf/geometry/blob/main/readme/twisted-bilayer-graphene-animation.gif)
![twisted bilayer graphene analysis](https://github.com/schmampf/geometry/blob/main/readme/twisted-bilayer-graphene-analysis.png)
