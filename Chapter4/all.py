from mpi4py import MPI
from reserved_pal import reverse_and_check_palindrome

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    strings = ["madam", "apple", "racecar", "python", "level"]

    my_string = strings[rank % len(strings)]

    reversed_s, is_palindrome = reverse_and_check_palindrome(my_string)

    all_reversed_strings = comm.allgather(reversed_s)

    print(f"[Rank {rank}/{size}] Original: '{my_string}' | Reversed: '{reversed_s}' | Palindrome: {is_palindrome}")
    
    if rank == 0:  
        print(f"All reversed strings gathered from all processes: {all_reversed_strings}")

if __name__ == "__main__":
    main()
