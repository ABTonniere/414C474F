#include <stdio.h>
int main() {
	int x, y, w, z;
	int puissance, entier, i;
	for (x = 1; x < 10; x++) {
		for (y = 1; y < 10; y++) {
			for (w = 1; w < 10; w++) {
				for (z = 1; z < 10; z++) {
					puissance = 1;
					i=0;
					while((i<y) && (i<z)){
						puissance *= x;
						puissance *= w;
						i++;
					}
					while((i<y)){
						puissance *= x;
						i++;
					}
					while((i<z)){
						puissance *= w;
						i++;
					}
					entier = (x * 1000) + (y * 100) + (w * 10) + z;
					if (puissance == entier) {
						printf("%d",entier);
					}
				}
			}
		}
	}
	return 0;
}

