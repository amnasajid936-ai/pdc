from mpi4py import MPI
from reserved_pal import reverse_and_check_palindrome  

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

strings = ["madam", "apple", "racecar", "python", "level"]

my_string = strings[rank % len(strings)]
reversed_s, is_palindrome = reverse_and_check_palindrome(my_string)
data_to_send = (my_string, reversed_s, is_palindrome)

gathered_data = comm.gather(data_to_send, root=0)

if rank == 0:
    print(f"Rank {rank} gathering data from other processes:\n")
    for i, (original, reversed_str, palindrome) in enumerate(gathered_data):
        print(f"Process {i}: Original='{original}', Reversed='{reversed_str}', Palindrome={palindrome}")
