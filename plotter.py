def plotter_fun(x,y,diff_y,fun_name):
    x_label='Vk'
    y_label='y'
    plt.plot(x,y,label='Function')
    plt.plot(x,diff_y,label='Diff_function')
    plt.grid()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(fun_name)
    plt.legend()
    plt.show()
