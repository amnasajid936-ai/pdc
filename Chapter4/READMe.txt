MPI Python Project: String Reversal and Palindrome Check

Overview:
This project demonstrates the use of MPI (Message Passing Interface) in Python using the mpi4py library. The goal is to perform parallel processing on strings to reverse them and check for palindromes. Various examples illustrate broadcasting, gathering, and point-to-point communication between processes.

Features:

Simple parallel string processing: Each MPI process selects a string, reverses it, and checks if it’s a palindrome.
Broadcasting example: Rank 0 sends data to all other ranks using bcast.
Gathering example: Each process sends results to rank 0 using gather.
Point-to-point communication: Selected ranks send and receive data using send and recv or sendrecv.
Supports multiple processes dynamically using rank-based selection of strings.