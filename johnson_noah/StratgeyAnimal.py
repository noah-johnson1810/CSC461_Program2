import types

from patterns import Behaviors


class Animal:
    def __init__(self, name, soundCnt = 1):
        self._name = name #still has to be public/protected for an outside strategy function to access
        self.__sound = None #step 1
        self.__soundName = None

    # set sound behavior, step 2
    def setSound( self, sound):
        self.__sound = sound

    #call behavior, step 3
    def makeNoise( self ):
        if(self.__sound != None):
            self.__sound()



    #strategy with deep binding----------------------------------------------------------------------
    #deep binding gives the function access to 'self',
    #although the members still need to be public or protected

    #set sound behavior
    def setSoundWithName( self, sound):
        create_bound_method = types.MethodType
        self.__soundName = create_bound_method(sound, self)

    #call for function with deep binding
    def makeNoiseWithName( self):
        if (self.__soundName != None):
            self.__soundName() # I do NOT pass in self

if __name__ == '__main__':
    dog = Animal("rufus")
    cat = Animal("fluffy")
    bird = Animal( "poly" )

    dog.setSound( Behaviors.dog )
    cat.setSound( Behaviors.cat )
    bird.setSound( Behaviors.bird )
    dog.makeNoise()
    cat.makeNoise()
    bird.makeNoise()




    print("\n\n\nnow with the name")
    dog.setSoundWithName( Behaviors.dogName )
    cat.setSoundWithName( Behaviors.catName )
    bird.setSoundWithName( Behaviors.birdName )
    dog.makeNoiseWithName( )
    cat.makeNoiseWithName( )
    bird.makeNoiseWithName( )
