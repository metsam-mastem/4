# Mathematical Foundations

## Vectors
x=(x1,…,xn)^T. Euclidean norm: ||x||₂=√(Σxi²). Dot product: a·b=Σai bi. Angle: cosθ=(a·b)/(||a|| ||b||). Use for geometric distances, embedding similarity, and layout forces; similarity is not proof of semantic equivalence.

## Matrices
Affine transform: x'=Ax+t. 2D rotation R(θ)=[[cosθ,-sinθ],[sinθ,cosθ]]. Transform composition uses matrix multiplication. Inverse exists only when A is invertible. D4 is the square's dihedral symmetry group: four rotations and four reflections. SSG defines D8 explicitly as the dihedral group of a regular octagon, order 16; record this convention in metadata.

## Graphs
G=(V,E). Adjacency Aij indicates a directed edge. Degree d(v)=Σu A(v,u); weighted strength s(v)=Σu w(v,u). Path cost is the sum of edge costs. Centrality describes topology, not truth or importance by itself.

## Rectangles
For w,h>0: area A=wh; perimeter P=2(w+h); diagonal d=√(w²+h²); aspect ratio r=max(w,h)/min(w,h)≥1; compactness C=4πA/P².
Ratio families (long/short): square 1; √2≈1.41421356237; √3≈1.73205080757; √5≈2.23606797750; golden φ=(1+√5)/2≈1.61803398875; double-square 2; 2√2≈2.82842712475. Note 2√2 is not √2.

A √2 rectangle split in half along its long side produces two similar √2 rectangles after rotation/scaling. This makes it useful for recursive page/tile layouts. √3 and √5 are additional geometric families; historical use must be evidenced case by case.

## Cuboids
For a,b,c>0: volume V=abc; surface area S=2(ab+bc+ca); space diagonal d=√(a²+b²+c²); aspect vector r=(a/b,b/c,c/a). Volume alone does not determine shape.

## π, Fibonacci, primes, irrationals
Circle circumference 2πr; area πr²; radial angle θi=2πi/n. Use π for radial layouts and circular timelines.
Fibonacci: F0=0,F1=1,Fn=Fn-1+Fn-2; ratios Fn+1/Fn converge to φ. Use as optional grid/scale sequence, not universal aesthetic law.
Primes 2,3,5,7,11,… may support deterministic non-critical indexing or sampling; they do not create security or visual balance automatically.
Store exact expressions such as sqrt(2), sqrt(3), sqrt(5), phi and pi separately from approximations, including precision and rounding mode.

## Error and tolerance
Absolute error ea=|xm-xt|. Relative error er=|xm-xt|/|xt| for xt≠0. Report measured ratio, target, absolute/relative deviation, uncertainty, and tolerance.
