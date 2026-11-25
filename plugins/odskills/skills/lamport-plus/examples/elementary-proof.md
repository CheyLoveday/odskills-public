# Reconstructing the parity proof

## Target LP-EX-01

For every integer $n$, if $n^2$ is even, then $n$ is even. The conclusion is
an integer divisibility claim. Evenness means $n=2k$ for some integer $k$.

## Governing idea

An even-square witness gives little direct information about $n$. The
contrapositive lets us choose a representation for $n$ itself. Squaring its
odd representation produces an explicit odd witness for $n^2$.

## Proof

- **⟨1⟩1.** Fix $n\in\mathbb Z$. By integer division with remainder by
  two, an integer that is not even is odd. It suffices to show that odd
  $n$ has odd square, because an integer is never both even and odd.
- **⟨1⟩2.** Suppose $n$ is odd. Choose the integer $k$ from its remainder-one
  representation $n=2k+1$. Multiplication gives
  $n^2=2(2k^2+2k)+1$. Since $2k^2+2k$ is an integer, this is an odd-square
  witness. The construction also applies to negative $n$ and $k$.
- **⟨1⟩3.** By ⟨1⟩1 and ⟨1⟩2, $n^2$ even forces $n$ even. QED.

## Reconstruction

1. Which implication is proved from the odd representation of $n$?
2. What value of $k$ is used for $n=-3$? Recover the square's witness.
3. Transfer task. For every integer $n$ prove that if $n^2$ is divisible
   by three then $n$ is divisible by three. Derive and use the possible
   remainders by three. Give a witness when the remainder is one or two
   and check that each resulting square has remainder one.

An optional proposed Lean target is
`theorem even_of_square_even (n : ℤ) (h : Even (n ^ 2)) : Even n`.
This is a signature sketch. Formal correspondence, compilation, axiom
inspection and independent replay are `NOT_RUN`.
