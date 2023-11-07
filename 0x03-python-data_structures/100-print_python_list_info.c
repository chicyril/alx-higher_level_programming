#include "Python.h"
/**
 * print_python_list_info - Prints information about python list objects
 * @p: PyObject pointer to print info about
 * Compile with:
 * gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared
 (* -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4
 (* 100-print_python_list_info.c
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
