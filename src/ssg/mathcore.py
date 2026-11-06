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
