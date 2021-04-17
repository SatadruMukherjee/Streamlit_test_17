# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#to run the code , use--streamlit run main.py
import streamlit as st
def hello():
    st.title("Hello World");#Main part title
    st.sidebar.title("Video Tutorials , Projects & Quiz");#Side part title
    #st.selectbox("Machine Learning", False)
    selection=st.sidebar.selectbox("What You want to Learn?",("Home","Machine Learning","Digital Signal Processing","Digital Image Processing"));#dropdown in sidebar
    if(selection=="Home"):
        st.markdown('''Hey Guyzz,
        
In this pandemic I trust everybody is at home staying safe.

Welcome to my channel!
                           
In my this channel , you can get videos related to ECE , MATLAB , JAVA , MULTISIM .

Hope my this channel will help you in boosting concepts.

Learn , Unlearn & Relearn😃

Thank You.

Have a great day!🙏''');  # Write something below the actula title
        st.write("https://www.youtube.com/channel/UCLAvd_eAgG651taJPdKxD1A/featured");
    if(selection=="Machine Learning"):
        st.markdown("Select one between below 2")
        if(st.checkbox("Theory of Machine Learning")):
            st.write('''Machine learning is an Artificial Intelligence technology where we give privilege to our computers to access our data and let them use the same data to learn for themselves.
                     
                     
It is basically getting a computer to perform a specific task without being programmed or instructed specifically to do so.

You can refer this playlist for learning all the mathematical concepts related to Applied Linear Algebra, Probability Theory and Random Processes & Statistics which are required for understanding the ML Algorithms''')
            st.write("https://youtube.com/playlist?list=PLLy_2iUCG87D1CXFxE-SxCFZUiJzQ3IvE");#function to write something
            st.write("You can refer this playlist for learning Machine Learning using Python");
            st.write("https://youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe")
            st.write("You can refer this playlist for learning Machine Learning using MATLAB");
            st.write("https://youtube.com/playlist?list=PLjfRmoYoxpNoaZmR2OTVrh-72YzLZBlJ2");

        elif st.checkbox("Want to test your understanding in ML?"):
            st.markdown("Select the algorithm ");
            if (st.checkbox("Introduction to Machine Learning")):
                st.write("https://youtu.be/qZD5-zKSPfw");
            elif (st.checkbox("Fundamentals of Regression")):
                st.write("https://youtu.be/unIYgvd8ehk");
            elif (st.checkbox("Intermediate Linear Regression Quiz")):
                st.write("https://youtu.be/O4nFcZMvJ6M");
            elif (st.checkbox("KNN Quiz (Part 1)")):
                st.write("https://youtu.be/WZHJ50XZERY");
            elif (st.checkbox("KNN Quiz (Part 2)")):
                st.write("https://youtu.be/fp4wAu-CmCI");
            elif (st.checkbox("Test your understanding on Support Vector Machines")):
                st.write("https://youtu.be/yg60x-RLQKs");
            elif (st.checkbox("PCA Interview Questions")):
                st.write("https://youtu.be/_Svym7xaipc");
            elif (st.checkbox("Unsupervised Machine learning MCQ questions")):
                st.write("https://youtu.be/HbeUYfzjRas");



    if(selection=="Digital Signal Processing"):
        st.write('''The world of science and engineering is filled with signals: images from remote space probes, voltages generated by the heart and brain, radar and sonar echoes, seismic vibrations, and countless other applications. Digital Signal Processing is the science of using computers to understand these types of data. This includes a wide variety of goals: filtering, speech recognition, image enhancement, data compression, neural networks, and much more. DSP is one of the most powerful technologies that will shape science and engineering in the twenty-first century. 
                    
So understanding DSP & implementing the concepts in software simulations is very important.''');

        st.write("Learn DSP with in-depth theoretical intuition");
        st.write("https://youtube.com/playlist?list=PLyqSpQzTE6M9py2rcGOLss74ZxBUvaC49");
        st.write("Learn DSP with MATLAB");
        st.write("https://youtube.com/playlist?list=PLjfRmoYoxpNr3w6baU91ZM6QL0obULPig");
    if(selection=="Digital Image Processing"):
        st.write('''Digital Image: Representing image in numbers so that it can be stored on computer. Image is stored on computer in the form of pixels. The resolution of an image x*y says how many rows it contains and how many columns it contains. And x multiplied by y gives the no. of pixels in an image. Each pixel again is represented in general by a byte if it is a gray scale (black and white image) and by 3 bytes if it is a color image ( a byte for each color Red, Green, Blue). So, basically a pixel is any point in an image.

Processing: Processing of an image is done for several purposes. Practical examples include Face Detection, Face Recognition, Number plate recognition, Hand written digit recognition, Object identification in images, Noise Removal, Finger Print Recognition and Computer Vision To achieve any of the above mentioned tasks, you have to process the digital image using particular algorithms.

Applications of Digital Image Processing that you see in everyday life:

Finger print scanners on all mobile phones, laptops , Face recognition software on all mobile phones, laptops,all picture editors like Picasa, Prisma, MS Paint, Photoshop,Finger print recognition used by Aadhar,Face detection using any camera app on mobile phones to detect faces.''');
        st.write("https://youtube.com/playlist?list=PLjfRmoYoxpNostbIaNSpzJr06mDb6qAJ0");








# Press the green button in the gutter to run the script.
hello()

#pip freeze > requirements.txt
