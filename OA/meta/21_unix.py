def solution(commands):
    # cp, ls, mv
    ans = [0,0,0]
    def dfs(index, visited):
        if index in visited:
            return 
        visited.add(index)
        command = commands[index]
        if command == "ls":
            ans[1] += 1
        elif command == "cp":
            ans[0] += 1
        elif command == "mv":
            ans[2] += 1
        else:
            # dfs
            number = int(command[1:]) - 1
            if number in range(len(commands)):
                dfs(number, visited)

    for i in range(len(commands)):
        dfs(i, set())
    return ans

commands1 = ["ls", "cp", "mv","mv","mv", "!1","!3", "!6"]
commands2 = ["ls", "cp", "mv", "!3", "mv", "!1", "!6"]

print(solution(commands1))  # Output: [1, 3, 4]
print(solution(commands2))  # Output: [1, 3, 3]