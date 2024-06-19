<script lang="ts">
    import Title from '$lib/title.svelte';
    import { ConnectedSocket } from '$lib/store';
    import { fade } from 'svelte/transition';

    async function GetDeviceInfo() {
        
    }

    async function MapModbusClient() {
        
    }
</script>

<div in:fade={{delay: 200, duration:200}} class="flex flex-col h-full">
    <div class="flex flex-col place-items-center border-2 border-gray-600 rounded-xl m-2 p-2">
        <Title>Tables</Title>
    </div>
    {#if $ConnectedSocket == null}
        <div class="flex flex-col justify-center items-center flex-grow text-2xl">
            <p>No connected socket, scan and connect from the networks page.</p>
            <a href="/network" class="border-2 px-10 py-2 mt-8 clickable border-white text-center">Networks</a>
        </div> 
    {:else}
        <div class="flex flex-row mx-auto p-2">
            <div class="flex-grow flex flex-col">
                {#each Array(64) as _}
                    <div class="flex flex-row">
                        {#each Array(32) as _}
                            <div class="h-2 w-2 bg-white m-0.5 hover:scale-150">
                            </div>
                        {/each}
                    </div>
                {/each}
            </div>
            <div class="flex-grow flex flex-col">
                {#each Array(64) as _}
                    <div class="flex flex-row">
                        {#each Array(32) as _}
                            <div class="h-2 w-2 bg-white m-0.5">
                            </div>
                        {/each}
                    </div>
                {/each}
            </div>
            <div class="flex-grow flex flex-col">
                {#each Array(64) as _}
                    <div class="flex flex-row">
                        {#each Array(32) as _}
                            <div class="h-2 w-2 bg-white m-0.5">
                            </div>
                        {/each}
                    </div>
                {/each}
            </div>
            <div class="flex-grow flex flex-col">
                {#each Array(64) as _}
                    <div class="flex flex-row">
                        {#each Array(32) as _}
                            <div class="h-2 w-2 bg-white m-0.5">
                            </div>
                        {/each}
                    </div>
                {/each}
            </div>
        </div>
    {/if}
</div>
