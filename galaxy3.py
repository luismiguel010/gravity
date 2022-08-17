from gravity_simulation.gravity import GravityField
from gravity_simulation.gravity import Body

field = GravityField()

#galaxy2 
field.generate_random(1120,mass=[1000,3000],r = [-5000,5000])
#field.add_body(Body(x0=1200,y0=1200,v_x=0,v_y=0,mass = 15000))
field.generate_random(5000,mass=[100,1500],r = [-5000,5000])

field.run(2000,C = 0.6)
field.save_animation(reduce_size_body=300,frames=150,title='galaxy')