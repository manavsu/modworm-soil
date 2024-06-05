<script lang="ts">
    import RandomSnake from "$lib/random_snake.svelte";
    export let message: string;
    import { submitted } from "../routes/store";

    function handleSubmit() {
        submitted.set(false);
    }
    </script>

<div class="flex flex-col h-dvh justify-center items-center">
    <h1 class="z-10 text-3xl">{message}</h1>
    <button class="z-10 text-5xl p-6" on:click={handleSubmit} >&larr;</button>
</div>

<RandomSnake />
