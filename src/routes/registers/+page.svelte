<script lang="ts">
    import Title from '$lib/title.svelte';
    import { ConnectedSocket, Working, CurrentTable} from '$lib/store';
    import { fade } from 'svelte/transition';
    import { BASE_URL } from '$lib/env'; 
    import LoadingSnake from '$lib/loading_snake.svelte';
    import Register from './register.svelte';

    let error: string | null = null;
</script>

<div in:fade={{delay: 200, duration:200}} class="flex flex-col h-full">
    <div class="flex flex-col place-items-center border-2 border-gray-600 rounded-xl m-2 p-2">
        {#if !error}
            <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
                <Title>Tables</Title>
            </div>
        {:else}
            <div in:fade={{delay: 200, duration:200}} class="flex flex-col justify-center h-14">
                <h2 class="text-center text-xl text-rose-900">{error}</h2>
            </div>
        {/if}
    </div>
    {#if !$CurrentTable}
        <div class="flex flex-col justify-center items-center flex-grow text-2xl">
            <p class="text-center">No selected table, select one from the tables page.</p>
            <a href="/tables" class="border-2 px-10 py-2 mt-8 clickable border-white text-center">Tables</a>
        </div> 
    {:else}
        {#each $CurrentTable as registerCnt}
            <Register/>
        {/each}
    {/if}
</div>