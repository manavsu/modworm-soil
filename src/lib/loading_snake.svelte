<script lang="ts">
	import '$lib/app.css';
	import { onMount } from 'svelte';
	import { BlockRepr } from '$lib/block_repr';
	import { Direction } from '$lib/direction';

	export let color: string = 'bg-white';
	export let tick_rate: number = 100;
	export let snake_size: number = 5;
	export let radius: number = 3;

	let snake_style: string = `w-3 h-3 absolute ${color}`;
	let delta: number = 20;
	let diameter_pixels: number = radius * 20 * 3;

	let snake: LoadingSnake;

	class LoadingSnake {
		size: number;
		blocks: BlockRepr[] = [];
		dir: Direction = Direction.Right;
		radius: number;
		delay: number;
		blocks_since_last_turn: number;
		in_loop: boolean = false;
        num_turns: number = 0;

		constructor(size: number, delta: number, radius: number) {
			this.size = size;
			this.radius = radius;
			this.delay = size - 1;
			this.blocks = [];
			this.blocks_since_last_turn = 0;

			for (let i = 0; i < size; i++)
				this.blocks.push(
					new BlockRepr(diameter_pixels / 2 - 6, diameter_pixels / 2 - 6, delta, 0, diameter_pixels, diameter_pixels)
				);
		}

		moveSnake() {
			if (this.blocks_since_last_turn >= this.radius * 2 || (!this.in_loop && this.blocks_since_last_turn >= radius)) this.pickNewDirection();
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
			if (this.delay > 0) this.delay--;
		}

		pickNewDirection() {
			if (this.dir == Direction.Up) this.dir = Direction.Right;
			else if (this.dir == Direction.Right) this.dir = Direction.Down;
			else if (this.dir == Direction.Down) this.dir = Direction.Left;
			else this.dir = Direction.Up;

            if (!this.in_loop && this.num_turns >= 1) this.in_loop = true;
			this.blocks_since_last_turn = 0;
            this.num_turns++;
		}
	}

	let isMounted = false;
	onMount(() => {
		snake = new LoadingSnake(snake_size, delta, radius);
		isMounted = true;
		setInterval(() => {
			snake.moveSnake();
			snake.blocks = [...snake.blocks];
		}, tick_rate);
	});
</script>

{#if isMounted}
<div style="height:{diameter_pixels}px; width:{diameter_pixels}px;" class="relative">
		{#each snake.blocks as block}
			<div class={snake_style} style="top: {block.y}px; left: {block.x}px;"></div>
		{/each}
</div>
{/if}
