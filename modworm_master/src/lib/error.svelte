<script lang="ts">
    import RandomSnake from "$lib/random_snake.svelte";
    export let message: string;
    export let path: string | null = null;
    </script>

<div class="flex flex-col h-dvh justify-center items-center">
    <h1 class="z-10 text-3xl">{message}</h1>
    {#if path != null}
        <a class="z-10 text-5xl p-6" href={path}>&larr;</a>
    {/if}
</div>

<RandomSnake />
