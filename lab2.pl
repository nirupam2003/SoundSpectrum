% Facts representing the graph as edges.
edge(a, b).
edge(b, d).
edge(b, e). %path
edge(a, c).
edge(c, f). %path

% BFS predicate.
bfs(Start, Goal, Visited) :- bfs_queue([Start], Goal, Visited). %add Visited and Goal

% Base case: Goal node found in the queue.
bfs_queue([Goal|_], Goal, _).

% Recursive case: Expand the front node and add its neighbors to the queue.
bfs_queue([Current|Rest], Goal, Visited) :-
    findall(Next, (edge(Current, Next), \+ member(Next, Visited)), Neighbors),
    append(Rest, Neighbors, NewQueue),
    bfs_queue(NewQueue, Goal, [Current|Visited]). %in append, in member

% Utility predicate to run BFS and print the result.
run_bfs(Start, Goal) :-
    bfs(Start, Goal, []),
    write('Goal reached: '), write(Goal), nl,
    write('Path: '), find_path(Start, Goal), nl. %find_path

% Utility predicate to find and print the path from Start to Goal.
find_path(Start, Goal) :-
    (Start == Goal ; edge(Start, Next)),
    write(Start),
    (Start == Goal ; write(' -> '), find_path(Next, Goal)).

% Example usage:
% run_bfs(a, d).