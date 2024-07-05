
<script lang="ts">
  import '$lib/app.css';
	import { Working } from '$lib/store';
  import LoadingSnake from '$lib/loading_snake.svelte';
  import { fade } from 'svelte/transition';
  import NetworkIcon from '$lib/icons/network_icon.svelte';
  import TablesIcon from '$lib/icons/tables_icon.svelte';
  import RegistersIcon from '$lib/icons/registers_icon.svelte';
  import { page } from '$app/stores'; 

  let path;
  $: path = $page.url.pathname
</script>

<style lang="postcss">
  :global(html) {
    @apply bg-black text-white;
    caret-color: white;
  }

  :global(.input) {
    @apply hover:scale-110 bg-white focus:scale-110 focus:outline-none active:text-white transition duration-300 rounded-xl bg-black;
  }

  :global(.clickable) {
    @apply hover:scale-110 active:scale-110 transition duration-300 rounded-xl;
  }
  
  * {
    @apply scrollbar scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-transparent;
  }
  </style>

<div class="flex flex-row h-dvh">
  <div class="flex flex-col">
    <div class="flex flex-col grow mt-5">
      <a class="p-4 hover:scale-110 transitino duration-300 {path == "/" ? "stroke-white" : "stroke-gray-500"}" href="/"><NetworkIcon/></a>
      <a class="p-4 hover:scale-110 transition duration-300 {path == "/tables" ? "stroke-white" : "stroke-gray-500"}" href="/tables"><TablesIcon/></a>
      <a class="p-4 hover:scale-110 transition duration-300 {path == "/registers" ? "stroke-white" : "stroke-gray-500"}" href="/registers"><RegistersIcon/></a>
    </div>
    <div class="mx-auto min-h-16">
      {#if $Working}
        <div transition:fade={{duration:300}}>
          <LoadingSnake radius={1}/>
        </div>
      {/if}
    </div>
  </div>
  <div class="border border-gray-500"/>
  <div class="flex-grow flex flex-col overscroll-contain overflow-auto">
          <slot />
  </div>
</div>