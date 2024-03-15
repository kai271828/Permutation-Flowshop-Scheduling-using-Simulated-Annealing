import numpy as np


class TFSProblem:
    def __init__(self, input_dir):
        with open(input_dir) as input_file:
            num_jobs, num_machines, _ = input_file.readline().split()

            self.num_jobs = int(num_jobs)
            self.num_machines = int(num_machines)

            table = []

            for i in range(self.num_machines):
                table.append(list(map(int, input_file.readline().split())))

            self.mj_table = np.array(table)

    @property
    def sol_length(self):
        return self.num_jobs

    def evaluate(self, sol):
        """
        Calculate the makespan for a given solution.
        """
        cache = np.zeros(self.num_machines)
        for job_id in sol:
            for machine_id in range(self.num_machines):
                if machine != 0:
                    cache[machine_id] = (
                        max(cache[machine - 1], cache[machine])
                        + self.mj_table[machine, job]
                    )
                else:
                    cache[machine] = cache[machine] + self.mj_table[machine, job]

            return cache[-1]


class Solution:
    def __init__(self, length):
        self.sol = np.random.permutation(length) + 1

    def __repr__(self):
        return ", ".join(map(str, self.sol.tolist()))

    def swap_neighborhood(self, i, j):
        """
        Return a new solution numpy array obtained by swap two elements
        """
        copy_sol = self.sol.copy()

        temp = copy_sol[i]
        copy_sol[i] = copy_sol[j]
        copy_sol[j] = temp

        return copy_sol

    def set_sol(self, sol):
        self.sol = sol
