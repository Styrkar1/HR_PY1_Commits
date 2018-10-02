#definition for music_func goes here
def music_func(mtype = "Classic Rock",group = "The Beatles",vocalist = "Freddie Mercury"):
    print("The best kind of music is " + mtype)
    print("The best music group is " + group)
    print("The best lead vocalist is " + vocalist)


def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()