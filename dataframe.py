import pandas as pd
import numpy as np

def main():
    print("Initializing dataframes...")
    array1=np.linspace(0,3,num=5)
    array2=3*array1+np.random.random(size=array1.size)
    tags = ['A','B','C','D','E']
    init_frame(array1,array2,tags)
    
def init_frame(a,b,tags):
    series1 = pd.Series(a,tags)
    series2 = pd.Series(b,tags)
    index = 'Row1 Row2'.split()
    frame = pd.DataFrame([series1,series2],index)
    print("| *Frame initialized!")
    print(frame)
    print("| *Exiting.")
    

if __name__=="__main__":
    main()