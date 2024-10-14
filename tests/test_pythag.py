import numpy as np 
import hypot.pythag

def test_add_nums():
    '''Test the function that adds to numbers'''

    # Arrange
    test_variable_a = 3
    test_variable_b = 4
    expected_output = 7

    # Act
    output = hypot.pythag.add_nums(test_variable_a, test_variable_b)

    # Assert
    assert output == expected_output

    # No cleanup needed
   
    
def test_add_nums_array():
    '''Test the function that adds to numbers'''

    # Arrange
    test_array_a = np.array([2, 5.7, 8])
    test_array_b = np.array([1.0, 1.0, 1.0])
    expected_output = np.array([3, 6.7, 9])

    # Act
    output = hypot.pythag.add_nums(test_array_a, test_array_b)

    # Assert
    assert np.allclose(expected_output, output)

    # No cleanup needed
    
    
def test_add_square_number():
    '''Test the function that adds to numbers'''

    # Arrange
    test_array_a = np.array([2, 5.7, 8])
    test_array_b = np.array([1.0, 1.0, 1.0])
    expected_output = np.array([3, 6.7, 9])

    # Act
    output = hypot.pythag.add_nums(test_array_a, test_array_b)

    # Assert
    assert np.allclose(expected_output, output)

    # No cleanup needed
    
    
def test_square_root():
    '''Test for the example function'''

    # Arrange
    test_variable_1 = 16
    expected_output = 4
    
    # Act
    output = hypot.pythag.square_root(test_variable_1)

    # Assert
    assert output == expected_output

    # No cleanup needed
    
    
def test_square_root_array():
    '''Test for the example function'''

    # Arrange
    test_array_1 = np.array([16, 49, 64])
    expected_output = np.array([4, 7, 8])
    
    # Act
    output = hypot.pythag.square_root(test_array_1)

    # Assert
    assert np.allclose(expected_output, output)

    # No cleanup needed
    
def test_calc_hypot():
    '''Test for the example function'''

    # Arrange
    test_variable_1 = 5.6
    test_variable_2 = 7.8
    expected_output = 9.6

    # Act
    output = hypot.pythag.calc_hypot(test_variable_1, test_variable_2)

    # Assert
    assert output == expected_output

    # No cleanup needed
    
def test_calc_hypot():
    '''Test for the example function'''

    # Arrange
    test_variable_1 = np.array([10, 30045, 6.9, 0.04])
    test_variable_2 = np.array([23, 2400, 8.9, 0.34])
    expected_output = np.array([25.08, 30140.7, 11.26, 0.34])

    # Act
    output = hypot.pythag.calc_hypot(test_variable_1, test_variable_2)

    # Assert
    assert np.allclose(expected_output, output, rtol= 1e-1)

    # No cleanup needed