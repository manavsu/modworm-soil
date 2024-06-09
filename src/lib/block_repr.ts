import { Direction } from "$lib/direction";

export class BlockRepr {
    x: number;
    y: number;
    delta: number;
    margin: number; 
    x_max: number;
    y_max: number;


    constructor(x: number, y: number, delta: number, margin: number, x_max: number, y_max: number) {
        this.x = x;
        this.y = y;
        this.delta = delta;
        this.margin = margin;
        this.x_max = x_max;
        this.y_max = y_max;
    }

    moveBlockDir(dir: Direction) {
        this.x = this.x + (dir === Direction.Right ? this.delta : dir === Direction.Left ? -this.delta : 0);
        this.y = this.y + (dir === Direction.Up ? this.delta : dir === Direction.Down ? -this.delta : 0);
        this.wrap();
    }

    moveBlock(x:number, y:number) {
        this.x = x;
        this.y = y;
    }

    wrap() {
        if (this.x < this.margin) this.x = this.x_max - this.margin;
        if (this.x > this.x_max - this.margin) this.x = this.margin;
        if (this.y < this.margin) this.y = this.y_max - this.margin;
        if (this.y > this.y_max - this.margin) this.y = this.margin;
    }
}