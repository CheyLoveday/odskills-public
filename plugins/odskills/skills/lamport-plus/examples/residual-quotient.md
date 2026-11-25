# A residual quotient of vector spaces

This example uses only finite-dimensional linear algebra.

## Target LP-EX-02

Let $A,W,P$ be subspaces of a finite-dimensional vector space $M$ over any
field. Let $J=P\cap W$, $V=A\cap W$, $U=J\cap V$, and
$q\colon M\to M/A$ be the quotient map. Then the maps induced by inclusion
and $q$ give the short exact sequence

$$
0\longrightarrow V/U\longrightarrow W/J\longrightarrow
q(W)/q(J)\longrightarrow0.
$$

Consequently the difference between $\dim(W/J)$ and $\dim(V/U)$ is
$\dim(q(W)/q(J))$.

## Governing idea

The inclusion compares two quotients by sending a representative to itself.
To measure what it misses, quotient out the part of $W$ that lies in $A$.
A class that vanishes after this projection can be moved into $A$ by
subtracting a representative from the original denominator $J$.

## Proof

- **⟨1⟩1.** Inclusion gives $i\colon V/U\to W/J$ by $v+U\mapsto v+J$.
  It is well defined since $U\subseteq J$. It is injective since
  $V\cap J=U$.
- **⟨1⟩2.** Projection gives $f\colon W/J\to q(W)/q(J)$ by
  $w+J\mapsto q(w)+q(J)$. It is well defined by the definition of $q(J)$,
  and onto because every element of $q(W)$ has a representative in $W$.
- **⟨1⟩3.** The image of $i$ lies in $\ker f$ because $V\subseteq A$.
  Conversely, given $w+J\in\ker f$, choose $j\in J$ with $q(w)=q(j)$.
  Then $w-j\in A\cap W=V$ and $(w-j)+J=w+J$. The class $(w-j)+U$
  is the required preimage under $i$.
- **⟨1⟩4.** The maps are linear by their representative formulas.
  Exactness from ⟨1⟩1–3 gives the claimed dimension difference by
  rank–nullity. QED.

## Challenge the denominator

A tempting candidate is $q(P)\cap q(W)$ in place of $q(J)$. In
$M=\mathbb F_2^4$ with standard basis $e_1,\dots,e_4$, take

$$
A=\operatorname{span}(e_1,e_2),\quad
W=\operatorname{span}(e_1,e_3,e_4),\quad
P=\operatorname{span}(e_2+e_3,e_4).
$$

Then $J=\operatorname{span}(e_4)$, $V=\operatorname{span}(e_1)$ and $U=0$.
The dimensions of $W/J$, $V/U$ and $q(W)/q(J)$ are $2,1,1$ respectively.
Since $q(e_2+e_3)=q(e_3)$, the proposed denominator is all of $q(W)$
and incorrectly gives complement dimension zero. Its witnesses can come
from $P$ or $W$ separately. The proof needs a witness in their intersection.

## Reconstruction and transfer

1. Reconstruct the witness in ⟨1⟩3 from the condition $f(w+J)=0$.
2. Determine when $i$ is surjective in terms of $q(J)$ and $q(W)$.
3. Assume $A\subseteq W$. Prove that $q(P)\cap q(W)=q(P\cap W)$ under
   that extra hypothesis. Identify the precise step the example above defeats.
