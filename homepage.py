from tkinter import *
from pandastable import Table, TableModel
from PIL import ImageTk, Image

def main():
    def loaddataset():
        #root.destroy()
        root1 = Tk()
        root1.geometry('1600x8000')
        root1.title('Dataset')

        f = Frame(root1)
        tb = Table(f)
        f.pack(fill=BOTH, expand=True)
        tb.importCSV('data.csv')
        tb.show()
        root1.mainloop()

    def annpage():
        def annrun():
            from ANN import first
            ann = first()
            label21 = Label(root2, text="Error : " + str(ann['Error']), bd='2', font=('helvetica', 15, 'bold'))
            label21.place(x=350, y=30)

            label22 = Label(root2, text="Test Accuracy : " + str(ann['Test Accuracy']), bd='2',
                            font=('helvetica', 15, 'bold'))
            label22.place(x=350, y=60)

            label23 = Label(root2, text="True Nagative : " + str(ann['True Nagative']), bd='2',
                            font=('helvetica', 15, 'bold'))
            label23.place(x=350, y=90)

            label24 = Label(root2, text="False Positive : " + str(ann['False Positive']), bd='2',
                            font=('helvetica', 15, 'bold'))
            label24.place(x=350, y=120)

            label25 = Label(root2, text="False Negative : " + str(ann['False Negative']), bd='2',
                            font=('helvetica', 15, 'bold'))
            label25.place(x=350, y=150)

            label26 = Label(root2, text="True Positive : " + str(ann['True Positive']), bd='2',
                            font=('helvetica', 15, 'bold'))
            label26.place(x=350, y=180)

            label27 = Label(root2, text="Missclassification Rate : " + str(ann['Missclassification Rate']), bd='2',
                            font=('helvetica', 15, 'bold'))
            label27.place(x=350, y=210)

            label28 = Label(root2, text="precision : " + str(ann['precision']), bd='2', font=('helvetica', 15, 'bold'))
            label28.place(x=350, y=240)

            label29 = Label(root2, text="recall : " + str(ann['recall']), bd='2', font=('helvetica', 15, 'bold'))
            label29.place(x=350, y=270)

            label201 = Label(root2, text="FScore : " + str(ann['FScore']), bd='2', font=('helvetica', 15, 'bold'))
            label201.place(x=350, y=300)

            label202 = Label(root2, text="Support : " + str(ann['Support']), bd='2', font=('helvetica', 15, 'bold'))
            label202.place(x=350, y=330)

            label203 = Label(root2, text="Sensitivity or TPR : " + str(ann['Sensitivity or TPR']), bd='2',
                             font=('helvetica', 15, 'bold'))
            label203.place(x=350, y=360)

            label204 = Label(root2, text="Specificity or TNR : " + str(ann['Specificity or TNR']), bd='2',
                             font=('helvetica', 15, 'bold'))
            label204.place(x=350, y=390)

            label205 = Label(root2,
                             text="False Positive Rate or Fallout : " + str(ann['False Positive Rate or Fallout']),
                             bd='2', font=('helvetica', 15, 'bold'))
            label205.place(x=350, y=420)

            label206 = Label(root2, text="False Negative Rate : " + str(ann['False Negative Rate']), bd='2',
                             font=('helvetica', 15, 'bold'))
            label206.place(x=350, y=450)

            label207 = Label(root2, text="False Discovery Rate : " + str(ann['False Discovery Rate']), bd='2',
                             font=('helvetica', 15, 'bold'))
            label207.place(x=350, y=480)

        def graph():
            root4 = Tk()
            img = ImageTk.PhotoImage(Image.open('h.png'), master=root4)
            vis_frame = LabelFrame(root4)
            vis_frame.pack()
            vis = Label(vis_frame, image=img)
            vis.image = img
            vis.pack()
            root4.mainloop()
        #root.destroy()
        root2 = Tk()
        root2.title("ANN")
        root2.geometry("1600x8000")

        runann = Button(root2, font=('arial', 16, 'bold'), text="Run ANN", activebackground="LightBlue", relief="raised", command=annrun, bd=10, bg="MediumPurple1")
        runann.place(x=600, y=600)

        showgraph = Button(root2, font=('arial', 16, 'bold'), text="Graph", activebackground="LightBlue", relief="raised", command=graph, bd=10, bg="MediumPurple1")
        showgraph.place(x=850, y=600)
        #print("ANN OUTPUT: ", ann)

    def svmpage():
        #root.destroy()
        from svm import second
        svmop, stochop = second()
        root3 = Tk()
        root3.title("SVM")
        root3.geometry("1600x8000")
        #print("ANN OUTPUT: ", svmop)
        #print("ANN OUTPUT: ", stochop)

        def graphsvm():
            root5 = Tk()
            img1 = ImageTk.PhotoImage(Image.open('SVM.png'), master=root5)
            img2 = ImageTk.PhotoImage(Image.open('Log_ROC_SVM.png'), master=root5)

            vis_frame = LabelFrame(root5)
            vis_frame.pack()

            vis = Label(vis_frame, image=img1)
            vis.image = img1
            vis.pack(side=LEFT)

            vis = Label(vis_frame, image=img2)
            vis.image = img2
            vis.pack(side=RIGHT)

            root5.mainloop()


        label30 = Label(root3, text="SVM Results : ", bd='2', font=('helvetica', 25, 'bold'))
        label30.place(x=150, y=40)

        label31 = Label(root3, text="Accuracy of SVM classifier on test set : " + str(svmop['Accuracy of Support vector Machines classifier on test set']), bd='2', font=('helvetica', 15, 'bold'))
        label31.place(x=50, y=100)

        label32 = Label(root3, text="Confusion Matrix : " + str(svmop['Confusion Matrix']), bd='2', font=('helvetica', 15, 'bold'))
        label32.place(x=50, y=140)

        label33 = Label(root3, text="Time took for training and predicting the results : " + str(svmop['Time took for training and predicting the results in seconds']), bd='2', font=('helvetica', 15, 'bold'))
        label33.place(x=50, y=220)

        label34 = Label(root3, text="Recall : " + str(svmop['Recall']), bd='2', font=('helvetica', 15, 'bold'))
        label34.place(x=50, y=260)

        label35 = Label(root3, text="F1- Score : " + str(svmop['F1- Score']), bd='2', font=('helvetica', 15, 'bold'))
        label35.place(x=50, y=300)

        label36 = Label(root3, text="Area Under the Curve : " + str(svmop['Area Under the Curve']), bd='2', font=('helvetica', 15, 'bold'))
        label36.place(x=50, y=340)

        svmgraph = Button(root3, font=('arial', 16, 'bold'), text="SVM Graphs", activebackground="LightBlue", relief="raised", command=graphsvm, bd=10, bg="MediumPurple1")
        svmgraph.place(x=150, y=500)

        def graphsg():
            root6 = Tk()
            img1 = ImageTk.PhotoImage(Image.open('SGD.png'), master=root6)
            img2 = ImageTk.PhotoImage(Image.open('Log_ROC.png'), master=root6)

            vis_frame = LabelFrame(root6)
            vis_frame.pack()

            vis = Label(vis_frame, image=img1)
            vis.image = img1
            vis.pack(side=LEFT)

            vis = Label(vis_frame, image=img2)
            vis.image = img2
            vis.pack(side=RIGHT)

            root6.mainloop()


        label300 = Label(root3, text="Stochastic Gradient Results : ", bd='2', font=('helvetica', 25, 'bold'))
        label300.place(x=850, y=40)

        label37 = Label(root3, text="Accuracy of SG classifier on test set : " + str(stochop['Accuracy of Stochastic Gradient classifier on test set']), bd='2', font=('helvetica', 15, 'bold'))
        label37.place(x=800, y=100)

        label38 = Label(root3, text="Confusion Matrix : " + str(stochop['Confusion Matrix']), bd='2', font=('helvetica', 15, 'bold'))
        label38.place(x=800, y=140)

        label39 = Label(root3, text="Time took for training and predicting the results : " + str(stochop['Time took for training and predicting the results in seconds']), bd='2', font=('helvetica', 15, 'bold'))
        label39.place(x=800, y=220)

        label301 = Label(root3, text="Recall : " + str(stochop['Recall']), bd='2', font=('helvetica', 15, 'bold'))
        label301.place(x=800, y=260)

        label302 = Label(root3, text="F1- Score : " + str(stochop['F1- Score']), bd='2', font=('helvetica', 15, 'bold'))
        label302.place(x=800, y=300)

        label303 = Label(root3, text="Area Under the Curve : " + str(stochop['Area Under the Curve']), bd='2', font=('helvetica', 15, 'bold'))
        label303.place(x=800, y=340)

        sggraph = Button(root3, font=('arial', 16, 'bold'), text="SG Graphs", activebackground="LightBlue", relief="raised", command=graphsg, bd=10, bg="MediumPurple1")
        sggraph.place(x=950, y=500)

        def graphother():
            root7 = Tk()
            img1 = ImageTk.PhotoImage(Image.open('histogram.png'), master=root7)
            img2 = ImageTk.PhotoImage(Image.open('correlation.png'), master=root7)

            vis_frame = LabelFrame(root7)
            vis_frame.pack()

            vis = Label(vis_frame, image=img1)
            vis.image = img1
            vis.pack(side=LEFT)

            vis = Label(vis_frame, image=img2)
            vis.image = img2
            vis.pack(side=RIGHT)

            root7.mainloop()

        othergraph = Button(root3, font=('arial', 16, 'bold'), text="Other Graphs", activebackground="LightBlue", relief="raised", command=graphother, bd=10, bg="MediumPurple1")
        othergraph.place(x=550, y=650)

    root = Tk()
    root.title("Home Page")
    root.geometry("1600x8000")

    label1 = Label(root, text="Breast Cancer Diagnosis using Artificial Neural Networks", bd='2', font=('helvetica', 25, 'bold'))
    label1.place(x=350,y=50)

    load = Button(root, font=('arial', 16, 'bold'), text="Load Dataset", activebackground="LightBlue", relief="raised", command=loaddataset, bd=10, bg="MediumPurple1")
    load.place(x=650, y=200)

    ann = Button(root, font=('arial', 16, 'bold'), text="ANN", activebackground="LightBlue", relief="raised", command=annpage, bd=10, bg="MediumPurple1")
    ann.place(x=700, y=300)

    svm = Button(root, font=('arial', 16, 'bold'), text="SVM", activebackground="LightBlue", relief="raised", command=svmpage, bd=10, bg="MediumPurple1")
    svm.place(x=700,y=400)

    root.mainloop()


if __name__ == '__main__':
    main()