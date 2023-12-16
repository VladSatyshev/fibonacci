### 1. Binary Exponentiation
[source](https://cp-algorithms.com/algebra/binary-exp.html)

**Цель**: Возведение в степень за $O(\log n)$.

**Идея**: 
1. Представить значение степени $n$ в бинарном виде. Длина двоичного представления равна $\lfloor\log_2{n}\rfloor + 1$.
2. Заметить, что за счет свойства степеней в худшем случае можно представить искомое значение как произведение из $\lfloor\log_2{n}\rfloor + 1$ чисел, т.е. $a^1 a^2 a^4 a^8 \cdots a^{2^{\lfloor\log_2{n}\rfloor}}$. Худший случай - когда двоичное представление содержит только единицы.
3. Заметить, что какждый последующий элемент в этом произведении вычисляется как квадрат предыдущего.

**Пример**: 
$$3^{13}=3^{1101_2}=3^{8+4+1}=3^8\cdot3^4\cdot3^1$$ 
При этом
$$3^1 = 3$$
$$3^2 = (3^1)^2$$
$$3^4 = (3^2)^2$$
$$3^8 = (3^4)^2$$

**Реализация**:
WIP

### 2. Фибоначчи через произведение матриц

$$
\begin{pmatrix}
f_{n}\\
f_{n-1}
\end{pmatrix}
=
\begin{pmatrix}
f_{n-1}+f_{n-2}\\
f_{n-1}+0
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix}
\begin{pmatrix}
f_{n-1}\\
f_{n-2}
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix}^2
\begin{pmatrix}
f_{n-2}\\
f_{n-3}
\end{pmatrix}
=
\cdots
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix}^{n-1}
\begin{pmatrix}
f_{1}\\
f_{0}
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix}^{n-1}
\begin{pmatrix}
1\\
0
\end{pmatrix}
$$

