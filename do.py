def do():


    myworld = World(population, initial_infection_rate, closeness, dimensions, speed, frequency, turns, no_doctors, length_of_immunity)
    myworld.populate_world(population, initial_infection_rate, closeness)

    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack(expand=YES, fill=BOTH)





    def paint(x, y, colour):
        python_green = colour
        x1, y1 = (x - 3), (y - 3)
        x2, y2 = (x + 3), (y + 3)
        w.create_oval(x1, y1, x2, y2, fill=python_green)



    def update(count):
        w.delete("all")
        myworld.update_world(count)

        infected, healthy, doctors = myworld.create_coord_list()

        for i in range(len(infected)):
            paint(infected[i, 0], infected[i, 1], '#FF0000')

        for i in range(len(healthy)):
            paint(healthy[i, 0], healthy[i, 1], '#0000FF')

        for i in range(len(doctors)):
            paint(doctors[i][0], doctors[i][1], '#00FF00')

        master.update()


    for i in range(turns):
        update(i)
        if i % train_new_doctor_frequency == 0:
            myworld.train_doctor()
        time.sleep(0.05)

    mainloop()


