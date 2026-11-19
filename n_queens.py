import copy


class Nqueens():
    def __init__(self):
        self._num_solutions = 0
        self._solutions = [] # Qui memorizzo le soluzioni buone

    def solve_problem(self, N):
        # chiamo la ricorsione la prima volta con soluzione parziale vuota
        self._recursion([], N)

    def _recursion(self, partial_sol, N):
        if len(partial_sol) == N:
            # Prima di considerare buona una soluzione, mi chiedo se per caso non l'abbia già trovata
            if self._solution_is_good(partial_sol):
                self._solutions.append(copy.deepcopy(partial_sol)) # Creo una copia "profonda" della soluzione
                print(partial_sol)
                self._num_solutions += 1
            return
        else:
            # partial_sol è una lista di tuple (row, col)
            for r in range(N):
                for c in range(N):
                    partial_sol.append((r,c))   # q coords
                    if self._pos_new_queen_is_accetable(partial_sol):
                        self._recursion(partial_sol, N) # Se non accettabile, abortiamo l'esplorazione
                    partial_sol.pop() # tolgo l'ultima regina

    # Funzione che mi dice se la posizione dell'ultima regina appesa sia valida oppure no
    def _pos_new_queen_is_accetable(self, partial_sol):
        last_queen = partial_sol[-1] # Ultima regina appena aggiunta
        for q in partial_sol[:len(partial_sol)-1]: # Escludo l'ultima regina aggiunta
            if q[0] == last_queen[0]:   # Sono sulla stessa riga, quindi non ammissibile
                return False
            elif q[1] == last_queen[1]: # Sono sulla stessa colonna, quindi non ammissibile
                return False
            elif abs(q[0] - last_queen[0]) == abs(q[1] - last_queen[1]): # Sono sulla stessa diagonale, quindi non ammissibile
                return False
        return True # Da non dimenticare


    def _solution_is_good(self, new_solution):
        new_set = set(new_solution)  # Confronto tra insiemi di regine
        for sol in self._solutions:
            if set(sol) == new_set:  # stesse regine, ordine diverso -> già trovata
                return False
        return True



if __name__ == "__main__":
    nq = Nqueens()
    nq.solve_problem(4)
    print(f"Num solutions: {nq._num_solutions}")
