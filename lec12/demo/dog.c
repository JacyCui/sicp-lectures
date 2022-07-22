#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
	int size;
	char color[20];
} Dog;

void bark(Dog* this) {
	if (this->size < 20) {
		printf("%s Dog: Wuwuwu!\n", this->color);
	} else {
		printf("%s Dog: Wooooooooof!\n", this->color);
	}
}

Dog* makeDog(int size, const char* color) {
	Dog* this = (Dog*)malloc(sizeof(Dog));
	this->size = size;
	strcpy(this->color, color);
	return this;
}

void delete(Dog* this) {
	free(this);
}

int main() {
	Dog* smallDog = makeDog(5, "Dark");
	Dog* bigDog = makeDog(20, "White");
	bark(smallDog);
	bark(bigDog);
	delete(smallDog);
	delete(bigDog);
	return 0;
}

