"""Dependency-free mathematical primitives for SSG."""
from dataclasses import dataclass
from math import pi, sqrt, hypot, cos, sin

@dataclass(frozen=True)
class Vec2:
    x: float
    y: float
    def __add__(self, other): return Vec2(self.x+other.x, self.y+other.y)
    def __sub__(self, other): return Vec2(self.x-other.x, self.y-other.y)
    def dot(self, other): return self.x*other.x+self.y*other.y
    def norm(self): return hypot(self.x,self.y)
    def scale(self, k): return Vec2(self.x*k,self.y*k)

@dataclass(frozen=True)
class Rect:
    width: float
    height: float
    def __post_init__(self):
        if self.width<=0 or self.height<=0: raise ValueError("dimensions must be positive")
    @property
    def area(self): return self.width*self.height
    @property
    def perimeter(self): return 2*(self.width+self.height)
    @property
    def diagonal(self): return hypot(self.width,self.height)
    @property
    def ratio(self): return max(self.width,self.height)/min(self.width,self.height)
    @property
    def compactness(self): return 4*pi*self.area/(self.perimeter**2)

@dataclass(frozen=True)
class Cuboid:
    a: float
    b: float
    c: float
    def __post_init__(self):
        if min(self.a,self.b,self.c)<=0: raise ValueError("dimensions must be positive")
    @property
    def volume(self): return self.a*self.b*self.c
    @property
    def surface_area(self): return 2*(self.a*self.b+self.b*self.c+self.c*self.a)
    @property
    def diagonal(self): return sqrt(self.a*self.a+self.b*self.b+self.c*self.c)
    @property
    def aspect_vector(self): return (self.a/self.b,self.b/self.c,self.c/self.a)

PHI=(1+sqrt(5))/2
PROPORTIONS={"square":1.0,"sqrt2":sqrt(2),"sqrt3":sqrt(3),"sqrt5":sqrt(5),
             "phi":PHI,"double_square":2.0,"two_sqrt2":2*sqrt(2)}

def fibonacci(n):
    if n<0: raise ValueError("n must be non-negative")
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def ratio_error(measured,target):
    if target==0: raise ValueError("target must be non-zero")
    absolute=abs(measured-target)
    return absolute,absolute/abs(target)

def rotate(point,radians):
    return Vec2(cos(radians)*point.x-sin(radians)*point.y,
                sin(radians)*point.x+cos(radians)*point.y)

def d4_orbit(point):
    x,y=point.x,point.y
    return (Vec2(x,y),Vec2(-y,x),Vec2(-x,-y),Vec2(y,-x),
            Vec2(-x,y),Vec2(x,-y),Vec2(y,x),Vec2(-y,-x))

def fit_ratio(rect,target,tolerance=0.01):
    if tolerance<0: raise ValueError("tolerance must be non-negative")
    return ratio_error(rect.ratio,target)[1]<=tolerance


def d8_matrices():
    """Return the 16 orthogonal symmetries of a regular octagon.

    Convention: rotations by k*pi/4 and each rotation composed with
    reflection across the x-axis. Matrices are rounded for stable keys.
    """
    from math import pi
    matrices = []
    reflection = ((1.0, 0.0), (0.0, -1.0))
    for k in range(8):
        theta = k * pi / 4
        c, s = cos(theta), sin(theta)
        rotation = ((c, -s), (s, c))
        matrices.append(tuple(tuple(round(v, 12) for v in row) for row in rotation))
        composed = (
            (rotation[0][0] * reflection[0][0] + rotation[0][1] * reflection[1][0],
             rotation[0][0] * reflection[0][1] + rotation[0][1] * reflection[1][1]),
            (rotation[1][0] * reflection[0][0] + rotation[1][1] * reflection[1][0],
             rotation[1][0] * reflection[0][1] + rotation[1][1] * reflection[1][1]),
        )
        matrices.append(tuple(tuple(round(v, 12) for v in row) for row in composed))
    return tuple(dict.fromkeys(matrices))


def apply_matrix(matrix, point):
    """Apply a 2x2 matrix represented by two row tuples to Vec2."""
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("matrix must be 2x2")
    return Vec2(matrix[0][0]*point.x + matrix[0][1]*point.y,
                matrix[1][0]*point.x + matrix[1][1]*point.y)


@dataclass(frozen=True)
class Vec3:
    """Three-dimensional Euclidean vector."""
    x: float
    y: float
    z: float
    def __add__(self, other): return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other): return Vec3(self.x-other.x, self.y-other.y, self.z-other.z)
    def dot(self, other): return self.x*other.x+self.y*other.y+self.z*other.z
    def cross(self, other):
        return Vec3(self.y*other.z-self.z*other.y,
                    self.z*other.x-self.x*other.z,
                    self.x*other.y-self.y*other.x)
    def norm(self): return sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def normalized(self):
        magnitude=self.norm()
        if magnitude==0: raise ValueError("zero vector cannot be normalized")
        return Vec3(self.x/magnitude,self.y/magnitude,self.z/magnitude)
    def scale(self, factor): return Vec3(self.x*factor,self.y*factor,self.z*factor)
