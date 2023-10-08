import matplotlib.pyplot as plt

def gen_pie_chart():
    labels = ['A', 'B', 'C']
    values = [48, 22, 30]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels= labels)
    plt.savefig('pie.png')
    plt.close()