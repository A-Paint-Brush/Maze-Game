import tkinter
import Game
window = tkinter.Tk()
window.title("Instructions")
window.geometry("400x400")
window.maxsize(400, 400)
window.minsize(400, 400)


def start():
    window.destroy()
    Game.Maze()


label = tkinter.Label(window, text="Instructions\nOnce you start the game, you will see a maze, and a cat at "
                                   "the\nstart of the maze. Once you click the cat, it will start following\nyour "
                                   "mouse cursor. Guide the cat to the golden ball at the\nend of the maze without "
                                   "touching the walls of the maze.\nThere are different colored tripwires throughout "
                                   "the maze. Some\ndo nothing when you touch them, but some kills you. If you "
                                   "die\nwhen you touch a tripwire, try taking a different route.")
label.pack()
button = tkinter.Button(window, text="Start Game", command=start)
button.pack()
window.mainloop()
