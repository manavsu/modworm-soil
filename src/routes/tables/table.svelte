<script lang="ts">
    import { fade } from 'svelte/transition';
	import LoadingSnake from "$lib/loading_snake.svelte";
	import Title from '$lib/title.svelte';

    export let table: []|null;
    export let title: string;

    function contains(i:number, j:number) {
        const start_index = ((i * 32) * 32) + (j * 32)
        const end_index = start_index + 31;
        if (table == null) return false;
        for (let cnt = 0; cnt < table?.length; cnt++) {
            if (start_index <= table[cnt][0] && table[cnt][0] <= end_index) {
                return true;
            }
            if (start_index <= table[cnt][1] && table[cnt][1] <= end_index) {
                return true;
            }
            if (table[cnt][0] <= start_index && start_index <= table[cnt][1]) {
                return true;
            }
            if (table[cnt][0] <= end_index && end_index <= table[cnt][1]) {
                return true;
            }
        }
        return false;
    }
</script>

    <div class="flex flex-col border h-full">
        <p class="text-2xl mx-auto p-5">{title}</p>
        {#if table == null}
            <div class="flex flex-col flex-grow border justify-center">
                <LoadingSnake />
            </div>
        {:else}
            <div in:fade class="flex flex-col items-center">
                {#each Array(64) as _, i}
                    <div class="flex flex-row w-fit">
                        {#each Array(32) as _, j}
                            <div class="h-2 w-2 {contains(i, j) ? "bg-white" : "bg-gray-500"} bg-white m-0.5 hover:scale-150"></div>
                        {/each}
                    </div>
                {/each}
            </div>
        {/if}
    </div>