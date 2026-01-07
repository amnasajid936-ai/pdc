from mpi4py import MPI
from reserved_pal import reverse_and_check_palindrome  

comm = MPI.COMM_WORLD
rank = comm.rank
print(f"My rank is: {rank}")

if rank == 0:
    data = 10000000
    destination_process = 4
    comm.send(data, dest=destination_process)
    print(f"Process {rank} sending data {data} to process {destination_process}")

if rank == 1:
    data = "madam"
    destination_process = 8
    reversed_s, is_palindrome = reverse_and_check_palindrome(data)
    print(f"Process {rank}: Original='{data}', Reversed='{reversed_s}', Palindrome={is_palindrome}")
    comm.send(data, dest=destination_process)
    print(f"Process {rank} sending data '{data}' to process {destination_process}")

if rank == 4:
    data = comm.recv(source=0)
    print(f"Process {rank} received data = {data}")

if rank == 8:
    data_received = comm.recv(source=1)
    reversed_s, is_palindrome = reverse_and_check_palindrome(data_received)
    print(f"Process {rank} received data = '{data_received}', Reversed='{reversed_s}', Palindrome={is_palindrome}")
