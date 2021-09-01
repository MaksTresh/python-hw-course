from collections import defaultdict


if __name__ == '__main__':
    shells_count = defaultdict(int)
    user_uids = {}

    with open('passwd') as passwd_file:
        for line in passwd_file:
            user, _, uid, *_, shell_name = line.strip().split(':')
            shells_count[shell_name] += 1
            user_uids[user] = uid

    groups = {}

    with open('group') as group_file:
        for line in group_file:
            group_name, *_, users = line.strip().split(':')
            if users:
                uuids = [user_uids[user] for user in users.split(',')]
                groups[group_name] = ','.join(uuids)
            else:
                groups[group_name] = ''

    with open('output.txt', 'w') as output:
        output.write('Shells:\n')
        for shell_name, count in shells_count.items():
            output.write(f'{shell_name} - {count} ; ')

        output.write('\n\n')

        output.write('Groups:\n')
        for group_name, users in groups.items():
            output.write(f'{group_name}:{users}, ')
