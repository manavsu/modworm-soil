import { Direction } from "$lib/direction";

export class BlockRepr {
    x: number;
    y: number;
    delta: number;
    margin: number; 


    constructor(x: number, y: number, delta: number, margin: number) {
        this.x = x;
        this.y = y;
        this.delta = delta;
        this.margin = margin;
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
        if (this.x < this.margin) this.x = window.innerWidth - this.margin;
        if (this.x > window.innerWidth - this.margin) this.x = this.margin;
        if (this.y < this.margin) this.y = document.body.scrollHeight - this.margin;
        if (this.y > document.body.scrollHeight - this.margin) this.y = this.margin;
    }
}