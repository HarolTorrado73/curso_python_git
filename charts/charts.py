import matplotlib as plt

def generate_pie_charts():
    lab = ['A', 'B', 'C']
    values = [200, 70, 120]

    fig, ax = plt.subplots()
    ax.pie(values, lab = lab)
    plt.savefig("diagrama.png")
    plt.close()