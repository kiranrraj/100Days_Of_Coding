import ctypes

class DynamicArray:
    """A dynamic array implementation using ctypes"""

    def __init__(self):
        """Create an empty array"""
        #private variables
        self._actualLen = 0
        self._actualCapacity = 1
        self._DynamicArr = self._createArray(self._actualCapacity)

    def _createArray(self, capacity):
        """Return new array with specified capacity"""
        return(capacity * ctypes.py_object)()

    def arrayLength(self):
        """Return the lenfth of the array"""
        return self._actualLen

    def getElem(self, index):
        """Get the value of the element at the position specified"""
        if not 0 <= index <self._actualCapacity:
            raise IndexError('Index out of bound error')
        return self._DynamicArr[index]

    def _resizeArr(self, capacity):
        """Create a new array"""
        _NewDynamicArr = self._createArray(capacity)
        for index in range(len(self._actualLen)):
            _NewDynamicArr[index] = self._DynamicArr[index]
        self._DynamicArr = _NewDynamicArr
        self._actualCapacity = capacity 

    def addElemeAt(self, pos,elem):
        """Add element to the array"""
        if 0 <= pos < self._actualLen:
            if self._actualLen == self._actualCapacity:
                _copyArr = self._createArray(self._actualLen * 2)
            for index in range(pos-2):
                _copyArr[index] = self._DynamicArr[index]
            self._DynamicArr[pos-1] = elem
            self._actualLen+=1
            for i in range(pos-1,self._actualLen):
                _copyArr[i] = self._DynamicArr[i]
            
            self._DynamicArr = _copyArr
        else:
            raise IndexError("Index out of bound error")

    def addElemeAtEnd(self, elem):
        """Add object to the array at the end"""
        if self._actualLen == self._actualCapacity:
            self._resizeArr(self._actualLen * 2)
        self._DynamicArr[self._actualLen] = elem
        self._actualLen += 1

    
        
print("----------------------------------------------------")
print("Option 1: Create an Array with capacity")
print("Option 2: Get the length of the array")
print("Option 3: Get the value at a index specified")
print("Option 4: Add an element at the specified position")
print("Option 5: Insert an element at the end")
print("----------------------------------------------------")
userInput = int(input("Enter your choice : "))

array_1 = DynamicArray()

if userInput == 1 :
    cap = int(input("Enter the capacity of the array :"))
    newArray = array_1._createArray(cap)
elif userInput == 2:
    print(f"{array_1.arrayLength()}")
elif userInput == 3:
    index = int(input("Enter the position to get the value"))
    print(f"{array_1.getElem(index)}")
elif userInput == 4:
    elem = int(input("Enter the element to enter"))
    pos = int(input("Enter the position where element need to be entered"))
    print(f"{array_1.addElemeAt(pos, elem)}")
elif userInput == 5:
    elem = int(input("Enter the element to enter"))
    print(f"{array_1.addElemeAtEnd(elem)}")
else :
    print("Please enter anyone from the above choice")
