<script lang="ts">
    import Title from "$lib/title.svelte";
    import { BASE_URL } from "$lib/env";
    import { fade } from 'svelte/transition';
    import { Network, Socket } from "$lib/network";
    import { onMount } from "svelte";
    import { Working, ConnectedSocket} from "$lib/store";
	import LoadingSnake from "$lib/loading_snake.svelte";
	import { Container } from "postcss";

    export let table: []|null;
    function contains(i:number, j:number) {
        const start_index = ((i * 32) * 32) + (j * 32)
        const end_index = start_index + 31;
        if (table == null) return false;
        for (let cnt = 0; cnt < table?.length; cnt++) {
            console.log(table[cnt][0], table[cnt][1], start_index, end_index);
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

{#if table == null}
    <LoadingSnake />
{:else}
    <div in:fade class="flex-grow flex flex-col">
        {#each Array(64) as _, i}
            <div class="flex flex-row">
                {#each Array(32) as _, j}
                    <div class="h-2 w-2 {contains(i, j) ? "bg-white" : "bg-gray-500"} bg-white m-0.5 hover:scale-150"></div>
                {/each}
            </div>
        {/each}
    </div>
{/if}