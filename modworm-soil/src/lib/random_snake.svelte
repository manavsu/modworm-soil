<script lang="ts">
    import "$lib/app.css";
    import { onMount } from 'svelte';
    import { BlockRepr } from "$lib/block_repr";
	import { Direction } from "$lib/direction";

    export let bg_color: string = "bg-gray-600";
    export let tick_rate: number = 100;
    export let snake_size: number = 20;

    let snake_style: string = `w-3 h-3 absolute ${bg_color}`;

    let margin: number = 20;
    let delta: number = 20;
    let dir_change_prob: number = .4;

    class RandomSnake {
        size: number;
        blocks: BlockRepr[];
        dir_change_prob: number;
        dir: Direction = Direction.Up;
        delay: number;
        blocks_since_last_turn: number;
        blocks_since_last_last_turn: number;
        initialized: boolean = false;
        
        constructor(size:number, dir_change_prob:number, margin:number, delta:number) {
            this.size = size;
            this.delay = size - 1;
            this.blocks = [];
            this.dir_change_prob = dir_change_prob;
            this.blocks_since_last_turn = 0;
            this.blocks_since_last_last_turn = 0;
        }

        moveSnake() {
            if (!this.initialized) {
                this.initialized = true;
                for (let i = 0; i < this.size; i++) this.blocks.push(new BlockRepr(window.innerWidth / 2, margin, delta, margin));
            }
            if (Math.random() < this.dir_change_prob) this.pickNewDirection();
            let last_dir = this.dir;
            let x = this.blocks[0].x;
            let y = this.blocks[0].y;
            this.blocks[0].moveBlockDir(this.dir);
            for (let i = 1; i < this.size - this.delay; i++) {
                let temp_x = this.blocks[i].x;
                let temp_y = this.blocks[i].y;
                this.blocks[i].moveBlock(x, y);
                x = temp_x;
                y = temp_y;
            }
            this.blocks_since_last_turn++;
            this.blocks_since_last_last_turn++;
            if (this.delay > 0) this.delay--;
        }

        pickNewDirection() {
            if (this.blocks_since_last_last_turn < this.size / 2) return;
            if (this.dir == Direction.Up || this.dir == Direction.Down)
                this.dir = Math.floor(Math.random() * 2) as Direction;
            else
                this.dir = Math.floor(Math.random() * 2) + 2 as Direction;
            this.blocks_since_last_last_turn = this.blocks_since_last_turn;
            this.blocks_since_last_turn = 0;
        }
    }

    let snake = new RandomSnake(snake_size, dir_change_prob, margin, delta);
    onMount(() => setInterval(() => {
        snake.moveSnake()
        snake.blocks = [...snake.blocks];
        }, tick_rate));
</script>


{#each snake.blocks as block}
    <div class={snake_style} style="top: {block.y}px; left: {block.x}px;"></div>
{/each}
