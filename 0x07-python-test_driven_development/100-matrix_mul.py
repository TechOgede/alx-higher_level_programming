
def matrix_mul(m_a, m_b):
    ''' Returns a matrix thats the product of m_a and m_b
        Args:
         m_a and m_b should be lists of lists of integers or floats
    '''
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    for list_a in m_a:
        if not isinstance(list_a, list):
            raise TypeError('m_a must be a list of lists')
        if not list_a:
            raise ValueError("m_a can't be empty")
        for num_a in list_a:
            if not isinstance(num_a, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
        len_list_a = len(m_a[0])
        if len_list_a != len(list_a):
            raise TypeError('each row of m_a must be of the same size')

    for list_b in m_b:
        if not isinstance(list_b, list):
            raise TypeError('m_b must be a list of lists')
        if not list_b:
            raise ValueError("m_b can't be empty")
        for num_b in list_b:
            if not isinstance(num_a, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
        len_list_b = len(m_b[0])
        if len_list_b != len(list_b):
            raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res_mat = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_ = 0
            for k in range(len(m_a)):
                sum_ += m_a[i][k] * m_b[k][j]
            row.append(sum_)
        res_mat.append(row)

    return res_mat
