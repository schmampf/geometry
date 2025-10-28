## Geometry

This project was inspired by an ethanol stove I borrowed from my neighbors during a heating outage in our apartment this October. Beyond its practical purpose of keeping us warm, the mesmerizing flame patterns sparked an interesting geometric challenge.

The basic concept of an ethanol stove is simple: ethanol fuel burns in a bowl, with a cover containing an adjustable aperture to control the flame. Traditionally, this adjustment is made by sliding a plate over the aperture, which can be dangerous due to proximity to the flames.

This project explores an alternative approach: using two superimposed plates with specially designed apertures. By rotating these plates relative to each other, we can dynamically control the effective cross-section of the opening. The design aims to create a small central opening that gradually expands with rotation, eventually transitioning into an outer ring pattern.

The geometry of these apertures is crucial for optimal combustion. Since oxygen can only penetrate a few centimeters into the ethanol vapor, controlling the aperture's diameter is essential. If the opening becomes too large, it leads to uneven burning and increased production of soot and other harmful emissions. This project implements mathematical models to optimize these geometric patterns for efficient and clean combustion.

### physics

crucial control paramter are:

$(x,y)$: crthesean coordinates

$(r, \theta)$: radial coordinates

$\theta$: the rotation angle. idealy in between 0 to 30°.

$r_com$: the radius, at which most of the area is open (center-of-mass). idealy from 0 to $r_\mathrm{max}$

$A_\mathrm{rel}$: the relative area of the aperture

i expect both paramter $r_com$ and $A_\mathrm{rel}$ two grow increasingly. from 0 to roughly 20 %.

### current state

A first idea comes from twisted bilayers of graphene, forming a nice Moiré Pattern.