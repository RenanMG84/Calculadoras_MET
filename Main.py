import tkinter as tk

#Parâmetros do frame root
root = tk.Tk()
root.title('Calculadora de estruturas metálicas')
root.geometry("400x300")

# Create the menu bar
menu_princ = tk.Menu(root)

#Menu Laminados
laminados = tk.Menu(menu_princ, tearoff=0)
laminados.add_command(label="Perfis W", command='')
laminados.add_command(label="Perfis tubulares", command='')
laminados.add_command(label="Cantoneiras", command='')
menu_princ.add_cascade(label="Perfis Laminados", menu=laminados)

#Menu Dobrados
dobrados = tk.Menu(menu_princ, tearoff= 0)
dobrados.add_command(label= 'Perfis Ue', command= '')
dobrados.add_command(label= 'Duplo Ue', command= '')
dobrados.add_command(label= 'Perfis U', command= '')
dobrados.add_command(label= 'Duplo U', command= '')
dobrados.add_command(label= 'Cantoneiras', command= '')
dobrados.add_command(label= 'Duplas cantoneiras', command= '')
menu_princ.add_cascade(label="Perfis Dobrados", menu=dobrados)

#Menu Ligações
ligacoes = tk.Menu(menu_princ, tearoff= 0)
#submenu Ligações Laminadas
lig_laminadas = tk.Menu(ligacoes, tearoff= 0)
lig_laminadas.add_command(label= 'Rígida com Chapa de topo', command= '')
lig_laminadas.add_command(label= 'Articulada com cantoneiras', command= '')
ligacoes.add_cascade(label= 'Ligações Laminadas', menu=lig_laminadas)
#submenu Ligações dobradas
lig_dobrados = tk.Menu(menu_princ, tearoff= 0)
lig_dobrados.add_command(label='Articulada com cantoneiras', command= '')
ligacoes.add_cascade(label= 'Ligações Dobradas', menu= lig_dobrados)
#posiciona o menu ligações no menu principal
menu_princ.add_cascade(label="Ligações", menu= ligacoes)

#Menu Placas de base
pb = tk.Menu(menu_princ, tearoff= 0)
pb.add_command(label='Placas Rígidas', command= '')
pb.add_command(label='Placas Articuladas', command= '')
pb.add_command(label='Placas Circulares', command= '')
pb.add_command(label='Placas Reforçadas', command= '')
menu_princ.add_cascade(label='Placas de Base', menu= pb)

#Menu ventos
ventos = tk.Menu(menu_princ, tearoff= 0)
ventos.add_command(label= 'Vento em barras isoladas', command= '')
ventos.add_command(label= 'Vento em coberturas isoladas', command= '')
ventos.add_command(label= 'Vento em placas', command= '')
ventos.add_command(label= 'Vento em pórticos', command= '')
ventos.add_command(label= 'Vento em treliças', command= '')
menu_princ.add_cascade(label= 'Ventos', menu= ventos)

#Menu Outros
outros = tk.Menu(menu_princ, tearoff= 0)
outros.add_command(label= 'Estabilidade Global', command= '')
outros.add_command(label= 'Chapas de piso', command= '')
outros.add_command(label= 'Linhas de corrente', command= '')
outros.add_command(label= 'Forças concentradas', command= '')
outros.add_command(label= 'Dimensionamento de erças', command= '')
outros.add_command(label= 'Dimensionamento de telhas', command= '')
menu_princ.add_cascade(label = 'Outros', menu= outros)

# Configure the root window to display the menu
root.config(menu=menu_princ)

root.mainloop()