import numpy as np

def sphere_volume(radius):
    """ computes the volume of a sphere.

    Parameters
    ----------
    radius : float
        radius of a sphere.

    Returns
    -------
    volume : float
        Volume of a sphere.

    """

    v = (4/3) * np.pi * radius**3
    return v

def sphere_area (radius):
    """ Computes the area of a sphere .
    Parameters
    ----------
    radius : float
        Radius of a sphere.

    Returns
    -------
    area : float
        Area of a sphere.

    """

    A = 4 * np.pi * radius**2
    return A
    
def main():
    radius = 4.5
    volume = sphere_volume(radius)
    area = sphere_area(radius)

    print("this sphere has a volume of: ")
    print(volume)
    print("this sphere has an area of: ")
    print(area)


if __name__ == "__main__":
    main()
    
