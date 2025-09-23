import numpy as np
import matplotlib.pyplot as plt


def conv_to_mat(mat):
    return [[mat[i][j][0] for j in range(len(mat[0]))] for i in range(len(mat))]


def find_path(mat):
    arrows = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            ver, hor, diag = mat[i][j][1]
            if ver:
                arrows.append((i, j, i - 1, j))
            if hor:
                arrows.append((i, j, i, j - 1))
            if diag:
                arrows.append((i, j, i - 1, j - 1))
    # print(arrows)
    return arrows


def show_mat(mat, A, B, title):
    matrix = np.array(conv_to_mat(mat))
    rows, cols = matrix.shape
    arrow_path = find_path(mat)

    b_tick_labels = [''] + list(B)
    a_tick_labels = [''] + list(A)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.matshow(matrix, cmap='YlGn')

    for i in range(rows):
        for j in range(cols):
            ax.text(j, i, str(matrix[i, j]), ha='center', va='center', color='red', fontsize=20)

    for start_row, start_col, end_row, end_col in arrow_path:
        ax.annotate(
            text='',
            xy=(end_col, end_row),
            xytext=(start_col, start_row),
            arrowprops=dict(
                arrowstyle='->',
                color='purple',
                lw=2,
                # connectionstyle='arc3,rad=0.3'
                shrinkA=15,
                shrinkB=12
            )
        )

    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))

    ax.set_xticklabels(a_tick_labels, fontsize=10)
    ax.set_yticklabels(b_tick_labels, fontsize=10)

    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    ax.set_title(title)
    ax.set_xlabel("A")
    ax.set_ylabel("B")

    plt.show()
