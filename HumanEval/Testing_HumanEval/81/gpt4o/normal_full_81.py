def numerical_letter_grade(grades):
    

   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade



def test():

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]) == ["A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.0]) == ["B+"] # New test case to catch the fault

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.3, 1.0]) == ['B-', 'D+']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]) == ["A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.8, 2.6]) == ['B', 'B-']
    assert numerical_letter_grade([2.1, 2.0]) == ['C+', 'C+']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.8, 2.0]) == ['B', 'C+']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.0]) == ['C+']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.4]) == ["A-"]  # New test case to detect the fault

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]) == ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "E"]

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.8, 3.6, 3.1, 2.8, 2.6, 2.1, 1.8, 1.6, 1.1, 0.8, 0.4, 0.0]) == ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.2]) == ['C+']  # This should fail because of the faulty elif condition

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([1.2]) == ['D+']  # This should pass if the code is correct

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.5]) == ["A-"]  # This test case detects the fault

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([1.7, 2.0, 2.1]) == ['C-', 'C-', 'C+']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.4]) == ["B-"]  # New test case to check the threshold around 2.3

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.0, 1.8, 1.2]) == ['B+', 'C', 'D+']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ["B", "B-"]
    assert numerical_letter_grade([1.9, 1.5]) == ["C", "C-"]
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ["D", "D-", "E"]
    assert numerical_letter_grade([1.6, 1.2]) == ["C-", "D+"]  # New test case to catch the faulty elif condition

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.0]) == ['C+']  # This case tests the edge value of 2.0
    assert numerical_letter_grade([1.3]) == ['C-']  # This case tests the edge value of 1.3
    assert numerical_letter_grade([1.0]) == ['D+']  # This case tests the edge value of 1.0

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.8, 3.4]) == ['B', 'A-']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.25]) == ['B+']  # Should be 'B+' but may incorrectly return 'B'

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.3]) == ["A-"]  # New test case to detect the fault

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.3, 3.4]) == ['A-', 'A-']  # This should pass if the code is correct

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.8, 1.9]) == ['B', 'C']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.7, 2.0]) == ['B', 'C+']  # This should detect the incorrect condition "elif gpa >= 2.7"

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([1.8, 1.2]) == ['C', 'D+']
    assert numerical_letter_grade([2.1, 0.8]) == ['C+', 'D']

    assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([2.1, 1.8]) == ['C+', 'C']  # New test case to detect the fault

