**Q4b**
*Manhattan*
Admissible -
Manhattan is the cost without walls. If there are no walls, then Manhattan successfully calculates without overestimating.
If there are walls, than the Manhattan cost is going to be less than the actual cost so it is still admissible.

Consistent -
Consistent, because the Manhattan distance decreases by at most 1 for each legal step.

*Euclidean*
Admissible -
This calculates a straight line distance between the start and the end. If there is a straight line that pacman can follow between
the start and the goal, then Euclidean sucessfully calculates without overestimating. If there isn't, the Euclidean will be shorter
because it doesn't have to follow game movement rules.

Consistent -
Moving one step decreases Euclidean distance by ≤ 1, so the triangle inequality guarantees consistency.

*Random*
Admissible -
If we have a way to guarentee that the shortest path is 10 * length then it is admissible, otherwise no.

Consistent -
This isn't consistent. With each iteration, the heuristic between two points will be different.

**Q5**

*DFS*
[SearchAgent] using function dfs
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 298 in 0.0 seconds
Search nodes expanded: 806
Pacman emerges victorious! Score: 212
Average Score: 212.0
Scores:        212.0
Win Rate:      1/1 (1.00)
Record:        Win

In this one, all the nodes in the left side dead end are explored despite there being no solution.
This happens because DFS explores as far down as it can. Those children end up being in the dead end.
So we end up with a lot of search nodes expanded, 806.

*BFS*
[SearchAgent] using function bfs
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 54 in 0.0 seconds
Search nodes expanded: 682
Pacman emerges victorious! Score: 456
Average Score: 456.0
Scores:        456.0
Win Rate:      1/1 (1.00)
Record:        Win

This one has a nice radial pattern. This happens because we open nodes one layer at a time.
We don't get stuck in the dead end here because we'll find the goal because expanding all of
the layers down in the dead end.

*UCS*
[SearchAgent] using function ucs
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 54 in 0.0 seconds
Search nodes expanded: 682
Pacman emerges victorious! Score: 456
Average Score: 456.0
Scores:        456.0
Win Rate:      1/1 (1.00)
Record:        Win

This one looks basically the same as BFS. This is because there are no extra coins or ghosts
in this maze. So the weight doesn't really have an impact.

*A star*
Manhattan -
[SearchAgent] using function astar and heuristic manhattanHeuristic
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 54 in 0.0 seconds
Search nodes expanded: 535
Pacman emerges victorious! Score: 456
Average Score: 456.0
Scores:        456.0
Win Rate:      1/1 (1.00)
Record:        Win

This pacman finds the solution by basically making two L shapes. It stays in straight lines if it can.
This matches with the Manhattan heuristic where it tries to find a straight legal path to the goal.
This heuristic also gives me the best result for fewest number of search nodes expanded.

Euclidian -
[SearchAgent] using function astar and heuristic euclideanHeuristic
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 54 in 0.0 seconds
Search nodes expanded: 550
Pacman emerges victorious! Score: 456
Average Score: 456.0
Scores:        456.0
Win Rate:      1/1 (1.00)
Record:        Win

This pacman has more of zig zag way of moving. This matches with the Euclidian heuristic which
prioritized diagnol paths.

Random -
[SearchAgent] using function astar and heuristic randomHeuristic
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 54 in 0.0 seconds
Search nodes expanded: 798
Pacman emerges victorious! Score: 456
Average Score: 456.0
Scores:        456.0
Win Rate:      1/1 (1.00)
Record:        Win

This path is really inconsistent. Some paths down in the dead end were explored. Other paths
weren't explored at all. Because there isn't a rhyme or reason, we end up with a LOT of search nodes expanded.
