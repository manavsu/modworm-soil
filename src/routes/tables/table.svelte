<script lang="ts">
    import { fade } from 'svelte/transition';
	import LoadingSnake from "$lib/loading_snake.svelte";
	import Title from '$lib/title.svelte';

    export let register_list: number[][]|null;
    export let title: string;

    function contains(i:number, j:number) {
        const start_index = ((i * 32) * 32) + (j * 32)
        const end_index = start_index + 31;
        if (register_list == null) return false;
        for (let cnt = 0; cnt < register_list?.length; cnt++) {
            if (start_index <= register_list[cnt][0] && register_list[cnt][0] <= end_index) {
                return true;
            }
            if (start_index <= register_list[cnt][0] + register_list[cnt][1] && register_list[cnt][0] + register_list[cnt][1] <= end_index) {
                return true;
            }
            if (register_list[cnt][0] <= start_index && start_index <= register_list[cnt][0] + register_list[cnt][1]) {
                return true;
            }
            if (register_list[cnt][0] <= end_index && end_index <= register_list[cnt][0] + register_list[cnt][1]) {
                return true;
            }
        }
        return false;
    }
</script>

<div class="flex flex-col h-full">
    <p class="text-2xl mx-auto p-3">{title}</p>
    {#if register_list == null}
        <div class="flex flex-col flex-grow justify-center">
            <LoadingSnake />
        </div>
    {:else}
        <div in:fade class="flex flex-col items-center">
            {#each Array(64) as _, i}
                <div class="flex flex-row w-fit">
                    {#each Array(32) as _, j}
                        <div class="h-1 w-1 {contains(i, j) ? "bg-white" : "bg-gray-600"} m-0.5"></div>
                    {/each}
                </div>
            {/each}
        </div>
    {/if}
</div>