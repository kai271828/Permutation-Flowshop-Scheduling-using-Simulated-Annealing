import numpy as np


class PFSProblem:
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
        machine_cache = np.zeros(self.num_machines)

        for job_id in sol:
            for machine_id in range(self.num_machines):
                if machine_id != 0:
                    machine_cache[machine_id] = (
                        max(machine_cache[machine_id - 1], machine_cache[machine_id])
                        + self.mj_table[machine_id, job_id]
                    )
                else:
                    machine_cache[machine_id] = (
                        machine_cache[machine_id] + self.mj_table[machine_id, job_id]
                    )

        return machine_cache[-1]


class Solution:
    def __init__(self, length=20, init_sol=None):
        if init_sol is not None:
            self._sol = init_sol.copy()
        else:
            self._sol = np.random.permutation(length)

    def __repr__(self):
        return ", ".join(map(lambda x: str(x + 1), self.sol.tolist()))

    def swap_neighborhood(self, i, j):
        """
        Return a new solution obtained by swap two elements
        """
        new_sol = Solution(init_sol=self.sol.copy())

        new_sol._set_sol_at(i, self.sol[j])
        new_sol._set_sol_at(j, self.sol[i])

        return new_sol

    @property
    def sol(self):
        return self._sol

    @sol.setter
    def sol(self, sol):
        self._sol = sol

    def _set_sol_at(self, index, num):
        self.sol[index] = num
