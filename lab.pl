edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c,f).

bfs(Start, Goal) :-
    bfs_queue([Start],Goal, []).

bfs_queue([Goal|_], Goal, _).

bfs_queue([Current|Rest], Goal, Visited) :-
    findall(Next, (edge(Current, Next), \+ member(Next, [Current|Visited])), Neighbors),
    append(Rest, Neighbors, NewQueue),
    bfs_queue(NewQueue, Goal, [Current|Visited]).


run_bfs(Start, Goal) :-
    bfs(Start, Goal),
    write('Goal reached: '),
    write(Goal), nl,
    write('Path: '),find_path(Start, Goal), nl.

find_path(Start, Start) :-
    write(Start).
find_path(Start, Goal) :-
    edge(Start, Next),
    write(Start), write(' -> '),
    find_path(Next, Goal).